---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dataSize.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# dataSize (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     dataSize: <string>,
     keyPattern: <document>,
     min: <document>,
     max: <document>,
     estimate: <boolean>
   }
)
```

## Command Fields

The command takes the following fields:

## Example

The following operation runs the :dbcommand:`dataSize` command on the `database.collection` collection, specifying a key pattern of `{field: 1}` with the lower bound of the range of keys to be examined being `{field: 10}` and the upper bound of the key to be examined being `{field: 100}`.

```javascript
db.runCommand({ dataSize: "database.collection", keyPattern: { field: 1 }, min: { field: 10 }, max: { field: 100 } })
```

This returns a document with the size in bytes for all matching documents. Replace `database.collection` with the database and collection from your deployment.

The amount of time required to return :dbcommand:`dataSize` depends on the amount of data in the collection.
