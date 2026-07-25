---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/cloneCollectionAsCapped.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
