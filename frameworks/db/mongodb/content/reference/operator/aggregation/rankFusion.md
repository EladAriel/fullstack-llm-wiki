---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/rankFusion.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $rankFusion (aggregation)

> **Important:** `$rankFusion` is only available for deployments that use MongoDB
8.0 or higher.

## Definition

## Syntax

The stage has the following syntax:

```javascript
{ $rankFusion: { 
    input: {
         pipelines: { 
             <myPipeline1>: <expression>,
             <myPipeline2>: <expression>,
             ...
         }
     },
     combination: { 
         weights: {
             <myPipeline1>: <numeric expression>,
             <myPipeline2>: <numeric expression>,
             ...
         }
     },
     scoreDetails: <bool>
 } }
```

### Command Fields

`$rankFusion` takes the following fields:

## Behavior

### Collections

You can only use `$rankFusion` with a single collection. You cannot use this aggregation stage at a database scope.

### De-Duplication

`$rankFusion` de-duplicates the results across multiple input pipelines in the final output. Each unique input document appears at most once in the `$rankFusion` output, regardless of the number of times that the document appears in input pipeline outputs.

### Input Pipelines

Each `input` pipeline must be both a Selection Pipeline and a Ranked Pipeline.

Selection Pipeline ``````````````````

A Selection Pipeline retrieves a set of documents from a collection without performing any modifications after retrieval. `$rankFusion` compares documents across different input pipelines which requires that all input pipelines output the same unmodified documents.

> **Note:** If you want to modify the documents that you search for with `$rankFusion`,
perform those modifications after the `$rankFusion` stage.

A selection pipeline must only contain the following stages:

Ranked Pipeline ```````````````

A ranked pipeline sorts or orders documents. `$rankFusion` uses the order of ranked pipeline results to influence the output ranking. Ranked pipelines must meet one of the following criteria:

- Begin with one of the following ordered stages:
- :pipeline:`$search`
- :pipeline:`$vectorSearch`
- :pipeline:`$geoNear`
- Contain an explicit :pipeline:`$sort` stage.
### Input Pipeline Names

Pipeline names in `input` must meet the following restrictions:

- Must not be an empty string
- Must not start with a `$`
- Must not contain the ASCII null character delimiter `\0` anywhere in the string
- Must not contain a `.`
### Reciprocal Rank Fusion (RRF) Formula

`$rankFusion` orders results according to the Reciprocal Rank Fusion (RRF) Formula. This stage places the RRF score for each document in the `score` metadata field of the output results. The RRF formula ranks documents with a combination of the following factors:

- The placement of documents in input pipeline results
- The number of times that a document appears in different input pipelines
- The `weights` of input pipelines.
For example, if a document has a high ranking in multiple pipeline result sets, the RRF score for that document would be higher than if that same document has the same ranking in some input pipelines, but is not present (or has a lower ranking) in the other pipelines

The  Reciprocal Rank Fusion (RRF) Formula is equivalent to the following algebraic operation:

.. figure:: /images/rrf-score.png

> **Note:** In this formula, 60 is a sensitivity parameter that MongoDB determined.

The below table contains the variables that the RRF formula uses:

Each term in the summation represents the appearance of a document `d` in one of the `input` pipelines. The total RRF score for `d` is the summation of each of these terms across all the input pipelines that `d` appears in.

RRF Calculation Example ```````````````````````

Consider a `$rankFusion` pipeline stage with one `$search` and one `$vectorSearch` input pipeline.

All input pipelines output the same 3 documents: `Document1`, `Document2`, and `Document3`.

The `$search` pipeline ranks the documents in the following order:

1. `Document3`
2. `Document2`
3. `Document1`
The `$vectorSearch` pipeline ranks the documents in the following order:

1. `Document1`
2. `Document2`
3. `Document3`.
`rankFusion` computes the RRF score for `Document1` through the following operation:

```none
RRFscore(Document1) = 1/(60 + search_rank_of_Document1) + (1/(60 + vectorSearch_rank_of_Document1))
RRFscore(Document1) = 1/63 + 1/61
RRFscore(Document1) = 0.0322664585
```

The `score` metadata field for `Document1` is `0.0322664585`.

### scoreDetails

If you set `scoreDetails` to `true`, `$rankFusion` creates a `scoreDetails` metadata field for each document. The `scoreDetails` field contains information about the final ranking.

> **Note:** When you set `scoreDetails` to `true`, `$rankFusion` sets the
`scoreDetails` metadata field for each document but does not automatically
output the `scoreDetails` metafield.
To view the `scoreDetails` metadata field, you must either:
- use a :pipeline:`$project` stage after `$rankFusion` to project the
  `scoreDetails` field
- use a :pipeline:`$addFields` stage after `$rankFusion` to add the
  `scoreDetails` field to your pipeline output

The `scoreDetails` field contains the following subfields:

Each array entry in the `details` field contains the following subfields:

.. include:: /includes/fact-scoreDetails-output-format.rst

For example, the following code blocks shows the `scoreDetails` field for a `$rankFusion` operation with `$search`, `$vectorSearch`, and `$match` input pipelines:

```js
{
   value: 0.030621785881252923,
   description: "value output by reciprocal rank fusion algorithm, computed as sum of weight * (1 / (60 + rank)) across input pipelines from which this document is output, from:"
   details: [
         {
            inputPipelineName: 'search',
            rank: 2,
            weight: 1,
            value: 0.3876491287,
            description: "sum of:",
            details: [... omitted for brevity in this example ...]
         },
         {
            inputPipelineName: 'vector',
            rank: 9,
            weight: 3,
            value: 0.7793490886688232,
            details: [ ]
         },
         {
            inputPipelineName: 'match',
            rank: 10,
            weight: 1,
            details: []
         }
   ]
 }
```

### Explain Results

MongoDB converts `$rankFusion` operations into a set of existing aggregation stages that, in combination, compute the output result prior to query execution. The `Explain Results <explain-results>` for a `$rankFusion` operation show the full execution of the underlying aggregation stages that `$rankFusion` uses to compose the final result.

## Examples
