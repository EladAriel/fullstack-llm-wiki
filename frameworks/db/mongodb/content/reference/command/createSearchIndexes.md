---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/createSearchIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# createSearchIndexes (database command)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndexes-description.rst

The `mongosh` method :method:`db.collection.createSearchIndex()` provides a wrapper around the `createSearchIndexes` database command.

.. include:: /includes/atlas-search-commands/atlas-only-db-command.rst

## Syntax

Command syntax:

```javascript
db.runCommand(
   {
      createSearchIndexes: "<collection name>",
      indexes: [
         {
            name: "<index name>",
            type: "<search index type>",
            definition: {
               /* search index definition fields */
            } 
        },
        ...
      ]
   }
)
```

## Command Fields

The `createSearchIndexes` command takes the following fields:

### Search Index Definition Syntax

.. include:: /includes/atlas-search-commands/search-index-definition-fields.rst

### Vector Search Index Definition Syntax

.. include:: /includes/atlas-search-commands/vector-search-index-definition-fields.rst

## Behavior

.. include:: /includes/atlas-search-commands/behavior/create-behavior.rst

## Access Control

.. include:: /includes/atlas-search-commands/access-control/create-access-control.rst

## Output

The `createSearchIndexes` command output resembles the following:

```javascript
{
   ok: 1,
   indexesCreated: [
      {
         id: "<index Id>",
         name: "<index name>"   
      }
   ]
}
```

> **Important:** The response field `ok: 1` indicates that the command was
successful. However, there may be a delay between when you receive
the response and when the created indexes are ready for use.
To see the status of your search indexes, use the
:pipeline:`$listSearchIndexes` aggregation stage.

## Examples

### Create a Search Index on All Fields

The following example creates a search index named `searchIndex01` on the `contacts` collection:

```javascript
db.runCommand( {
   createSearchIndexes: "contacts",
   indexes: [
      {
         name: "searchIndex01",
         definition: { mappings: { dynamic: true } }
      }
   ]
} )
```

The index definition specifies `mappings: { dynamic: true }`, which means that the index contains all fields in the collection that have `supported data types <bson-data-chart>`.

### Create a Search Index with a Language Analyzer

A language analyzer introduces stop-words, which are words that are not significant enough to be indexed.

The following example creates a search index named `frenchIndex01` on the `cars` collection, and specifies the `lucene.french` analyzer on the `fr` field:

```javascript
db.runCommand( {
   createSearchIndexes: "cars",
   indexes: [
      {
         name: "frenchIndex01",
         definition: {
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
      }
   ]
} )
```

To learn more about language analyzers, see `ref-language-analyzers`.

### Create Multiple Search Indexes

The following command creates two search indexes on the `products` collection, `searchIndex02` and `searchIndex03`:

```javascript
db.runCommand( {
   createSearchIndexes: "products",
   indexes: [
      {
         name: "searchIndex02",
         definition: {
            mappings: {
               fields: {
                  title: {
                     type: "string",
                     analyzer: "lucene.simple"
                  }
               }
            }
         }
      },
      {
         name: "searchIndex03",
         definition:
            {
               mappings: { dynamic: true }
            }
      }
   ]
} )
```

`searchIndex02` uses a `simple analyzer <ref-simple-analyzer>` on the `title` field. The simple analyzer divides text into searchable terms based on non-letter characters, such as whitespace, punctuation, or digits.

`searchIndex03` uses a dynamic field mapping, meaning the index contains all fields in the collection that have `supported data types <bson-data-chart>`.

### Create a Vector Search Index

The following example creates a vector search index named `vectorSearchIndex01` on the `movies` collection:

```javascript
db.runCommand( {
   createSearchIndexes: "movies",
   indexes: [
      {
         name: "vectorSearchIndex01",
         type: "vectorSearch",
         definition: {
            fields: [
               {
                  type: "vector",
                  numDimensions: 1,
                  path: "genre",
                  similarity: "cosine"
               }
            ]
         }
      }
   ]
} )
```

The vector search index contains one dimension and indexes the `genre` field.

## Learn More

- :pipeline:`$vectorSearch` aggregation stage
- `Tutorial: Semantic Search <vector-search-quick-start>`
- :atlas:`{+avs+} Changelog </atlas-vector-search/changelog/>`
