---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetSyncFrom.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
