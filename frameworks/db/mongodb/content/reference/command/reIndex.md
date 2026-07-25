---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/reIndex.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# reIndex (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     reIndex: <collection> 
   }
)
```

## Command Fields

The command takes the following fields:

## Behavior

For MongoDB 5.0 or later, :dbcommand:`reIndex` may only be run on `standalone` instances.

### Resource Locking

:dbcommand:`reIndex` obtains an exclusive (W) lock on the collection and blocks other operations on the collection until it completes.

For more information on locking in MongoDB, see `/faq/concurrency`.
