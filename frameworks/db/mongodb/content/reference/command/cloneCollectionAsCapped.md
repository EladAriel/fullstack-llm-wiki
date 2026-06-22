---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/cloneCollectionAsCapped.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# cloneCollectionAsCapped (database command)

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
    cloneCollectionAsCapped: <existing collection>, 
    toCollection: <capped collection>,
    size: <capped size>,
    writeConcern: <document>,
    comment: <any>  
  }
)
```

### Command Fields

The command takes the following fields:

The command copies an `existing collection` and creates a new `capped collection` with a maximum size specified by the `capped size` in bytes.

To replace the original non-capped collection with a capped collection, use the :dbcommand:`convertToCapped` command.

## Behavior

If the `capped size` is less than the size of the source collection, then not all documents in the source collection will exist in the destination capped collection.

.. include:: /includes/fact-database-lock.rst
