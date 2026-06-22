---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/scoreFusion.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $scoreFusion (aggregation)

> **Important:** `$scoreFusion` is only available for deployments that use MongoDB
8.2+.

## Definition

## Syntax

The stage has the following syntax:

```javascript
{ $scoreFusion: { 
    input: {
      pipelines: { 
            <input-pipeline-name>: <expression>,
            <input-pipeline-name>: <expression>,
            ...
      },
      normalization: "none|sigmoid|minMaxScaler"
    },
    combination: { 
      weights: {
            <input-pipeline-name>: <numeric expression>,
            <input-pipeline-name>: <numeric expression>,
            ...
      },
      method: "avg|expression",
      expression: <expression>
    }
} }
```

### Fields

`$scoreFusion` takes the following fields:

## Behavior

### Collections

You can only use `$scoreFusion` with a single collection. You cannot use this aggregation stage at a database scope.

### De-Duplication

`$scoreFusion` de-duplicates the results across multiple input pipelines in the final output. Each unique input document appears at most once in the `$scoreFusion` output, regardless of the number of times that the document appears in input pipeline outputs.

### Input Pipelines

Each `input` pipeline must be both a Selection Pipeline and a Scoring Pipeline.

Selection Pipeline ``````````````````

A Selection Pipeline retrieves a set of documents from a collection without performing any modifications after retrieval. `$scoreFusion` compares documents across different input pipelines which requires that all input pipelines output the same unmodified documents.

A selection pipeline must only contain the following stages:

Scoring Pipeline ````````````````

A scoring pipeline sorts or orders documents based on the score of the documents. `$scoreFusion` uses the order of scored pipeline results to influence the output scores. Scoring pipelines must meet one of the following criteria:

- Begin with one of the following ordered stages:
- :pipeline:`$search`
- :pipeline:`$vectorSearch`
- :pipeline:`$match` with legacy text search
- :pipeline:`$geoNear`
- Contain an explicit :pipeline:`$score` stage if the preceding pipeline
doesn't inherently return a score.

### Input Pipeline Names

Pipeline names in `input` must meet the following restrictions:

- Must not be an empty string
- Must not start with a `$`
- Must not contain the ASCII null character delimiter `\0` anywhere in the string
- Must not contain a `.`
### scoreDetails

If you set `scoreDetails` to `true`, `$scoreFusion` creates a `scoreDetails` metadata field for each document. The `scoreDetails` field contains information about the final ranking.

> **Note:** When you set `scoreDetails` to `true`, `$scoreFusion` sets the
`scoreDetails` metadata field for each document. By default, it
doesn't automatically output the `scoreDetails` metafield.
To view the `scoreDetails` metadata field, you must explicitly set
it through the :expression:`$meta` expression in a stage like
:pipeline:`$project`, :pipeline:`$addFields`, or :pipeline:`$set`.

The `scoreDetails` field contains the following subfields:

Each array entry in the `details` field contains the following subfields:

.. include:: /includes/fact-scoreDetails-output-format.rst

### Explain Results

MongoDB converts `$scoreFusion` operations into a set of existing aggregation stages that, in combination, compute the output result prior to query execution. The `Explain Results <explain-results>` for a `$scoreFusion` operation show the full execution of the underlying aggregation stages that `$scoreFusion` uses to compose the final result.

## Examples

This example uses a collection with embeddings and text fields. Create `search` and `vectorSearch` type indexes on the collection.

The following index definition automatically indexes all the dynamically indexable fields in the collection for running :pipeline:`$search` queries against the indexed fields.

```js
db.embedded_movies.createSearchIndex(
   "<INDEX_NAME>",
   {
      mappings: { dynamic: true }
   }
)
```

The following index definition indexes the field with the embeddings in the collection for running :pipeline:`$vectorSearch` queries against that field.

```js
db.embedded_movies.createSearchIndex(
   "<INDEX_NAME>", 
   "vectorSearch", 
   {
      "fields": [
         {
            "type": "vector",
            "path": "<FIELD_NAME>",
            "numDimensions": <NUMBER_OF_DIMENSIONS>,
            "similarity": "dotProduct"
         }
      ]
   }
);
```

The following aggregation pipeline uses `$scoreFusion` with the following input pipelines:

```js
db.embedded_movies.aggregate( [
   {
      $scoreFusion: {
         input: {
            pipelines: {
               searchOne: [
                  {
                     "$vectorSearch": {
                        "index": "<INDEX_NAME>",
                        "path": "<FIELD_NAME>",
                        "queryVector": <QUERY_EMBEDDINGS>,
                        "numCandidates": <NUMBER_OF_NEAREST_NEIGHBORS_TO_CONSIDER>,
                        "limit": <NUBMER_OF_DOCUMENTS_TO_RETURN>
                     }
                  }
               ],
               searchTwo: [
                  {
                     "$search": {
                        "index": "<INDEX_NAME>",
                        "text": {
                           "query": "<QUERY_TERM>",
                           "path": "<FIELD_NAME>"
                        }
                     }
                  },
               ]
            },
            normalization: "sigmoid"
         },
         combination: {
            method: "expression",
            expression: {
               $sum: [
                 {$multiply: [ "$$searchOne", 10]}, "$$searchTwo"
               ]
            }
         },
         "scoreDetails": true
      }
   },
   {
      "$project": {
         _id: 1,
         title: 1,
         plot: 1,
         scoreDetails: {"$meta": "scoreDetails"}
      }
   },
   { $limit: 20 }
] )
```

This pipeline performs the following actions:

- Executes the `input` pipelines
- Combines the returned results
- Outputs the first 20 documents which are the top 20 ranked results of
the `$scoreFusion` pipeline
