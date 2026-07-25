---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropSearchIndex.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# dropSearchIndex (database command)

## Definition

.. versionadded:: 7.0 (Also available starting in 6.0.7)

.. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst

The `mongosh` method :method:`db.collection.dropSearchIndex()` provides a wrapper around the `updateSearchIndex` database command.

.. include:: /includes/atlas-search-commands/atlas-only-db-command.rst

## Syntax

Command syntax:

```javascript
db.runCommand(
   {
      dropSearchIndex: "<collection name>",
      id: "<index Id>",
      name: "<index name>"
   }
)
```

## Command Fields

The `dropSearchIndex` command takes the following fields:

## Behavior

.. include:: /includes/atlas-search-commands/behavior/delete-behavior.rst

## Access Control

.. include:: /includes/atlas-search-commands/access-control/drop-access-control.rst

## Output

A successful `dropSearchIndex` command returns the following:

```javascript
{
   ok: 1
}
```

## Example

The following example deletes a search index named `searchIndex01` on the `contacts` collection:

```javascript
db.runCommand( {
   dropSearchIndex: "contacts",
   name: "searchIndex01"
} )
```
