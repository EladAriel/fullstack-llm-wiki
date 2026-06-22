---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.createSearchIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# db.collection.createSearchIndex() (mongosh method)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndex-method.rst

.. include:: /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

## Syntax

Command syntax:

```javascript
db.<collection>.createSearchIndex(
   <name>,
   <type>,
   {
      <definition>
   }
)
```

## Command Fields

`createSearchIndex()` takes these fields:

### Search Index Definition Syntax

.. include:: /includes/atlas-search-commands/search-index-definition-fields.rst

### Vector Search Index Definition Syntax

.. include:: /includes/atlas-search-commands/vector-search-index-definition-fields.rst

## Behavior

.. include:: /includes/atlas-search-commands/behavior/create-behavior.rst

## Access Control

.. include:: /includes/atlas-search-commands/access-control/create-access-control.rst

## Examples

### Create a Search Index on All Fields

The following example creates a search index named `searchIndex01` on the `movies` collection:

```javascript
db.movies.createSearchIndex(
   "searchIndex01",
   { mappings: { dynamic: true } }
)
```

The index definition specifies `mappings: { dynamic: true }`, which means that the index contains all fields in the collection that have `supported data types <bson-data-chart>`.

### Create a Search Index with a Language Analyzer

A language analyzer introduces stop-words, which are words that are not significant enough to be indexed.

The following example creates a search index named `frenchIndex01` on the `cars` collection, and specifies the `lucene.french` analyzer on the `fr` field:

```javascript
db.cars.createSearchIndex(
   "frenchIndex01",
   {
      mappings: {
         fields: {
            subject: {
               fields: {
                  fr: {
                     analyzer: "lucene.french",
                     type: "string"
                  }
               },
               type: "document"
            }
         }
      }
   }
)
```

To learn more about language analyzers, see `ref-language-analyzers`.

### Create a Search Index with the Default Name

The following `createSearchIndex()` method only specifies the index definition and omits the index name. The command creates a search index with the name `default` on the `food` collection:

```javascript
db.food.createSearchIndex(
   {
      mappings: {
         fields: {
            title: {
               type: "string"
            }
         }
      }
   }
)
```

### Create a Vector Search Index

The following example creates a vector search index named `vectorSearchIndex01` on the `movies` collection:

```javascript
db.movies.createSearchIndex(
   "vectorSearchIndex01",
   "vectorSearch",
   {
      fields: [
         {
            type: "vector",
            numDimensions: 1,
            path: "genre",
            similarity: "cosine"
         }
      ]
   }
)
```

The vector search index contains one dimension and indexes the `genre` field.

## Learn More

- :pipeline:`$vectorSearch` aggregation stage
- `Tutorial: Semantic Search <vector-search-quick-start>`
- :atlas:`{+avs+} Changelog </atlas-vector-search/changelog/>`
