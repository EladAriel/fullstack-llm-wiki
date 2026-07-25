---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetSyncFrom.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# replSetSyncFrom (database command)

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     replSetSyncFrom: "hostname<:port>" 
   }
 )
```

## Command Fields

The command takes the following field:

## Behavior

.. include:: /includes/extracts/rsSyncFrom-behavior-command.rst

For more information the use of :dbcommand:`replSetSyncFrom`, see `/tutorial/configure-replica-set-secondary-sync-target`.
