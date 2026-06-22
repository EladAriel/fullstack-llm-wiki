---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/updateSearchIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# updateSearchIndex (database command)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst

The `mongosh` method :method:`db.collection.updateSearchIndex()` provides a wrapper around the `updateSearchIndex` database command.

.. include:: /includes/atlas-search-commands/atlas-only-db-command.rst

## Syntax

Command syntax:

```javascript
db.runCommand(
   {
      updateSearchIndex: "<collection name>",
      id: "<index Id>",
      name: "<index name>",
      type: "search | vectorSearch",
      definition: {
         /* search index definition fields */
      }
   }
)
```

## Command Fields

The `updateSearchIndex` command takes the following fields:

### Search Index Definition Syntax

.. include:: /includes/atlas-search-commands/search-index-definition-fields.rst

## Behavior

.. include:: /includes/atlas-search-commands/behavior/update-behavior.rst

## Access Control

.. include:: /includes/atlas-search-commands/access-control/update-access-control.rst

## Output

A successful `updateSearchIndex` command returns the following:

```javascript
{
   ok: 1
}
```

> **Important:** The response field `ok: 1` indicates that the command was successful.
However, there may be a delay between when you receive the response and
when the updated index is ready and replaces the original index.
To see the status of your search indexes, use the
:pipeline:`$listSearchIndexes` aggregation stage.

## Example

The following example updates a search index named `searchIndex01` on the `contacts` collection:

```javascript
db.runCommand( {
   updateSearchIndex: "contacts",
   name: "searchIndex01",
   definition:
      {
         mappings: { dynamic: true },
         storedSource: {
            exclude: [ "directors", "imdb.rating" ]
         }
      }
} )
```
