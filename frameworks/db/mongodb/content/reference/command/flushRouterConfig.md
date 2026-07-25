---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/flushRouterConfig.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# flushRouterConfig (database command)

## Definition

> **Note:** Running :dbcommand:`flushRouterConfig` is no longer required after executing
:dbcommand:`movePrimary`, :dbcommand:`dropDatabase`, or
:method:`db.collection.getShardDistribution()`. These
commands now automatically refresh a sharded cluster's routing table as
needed when run.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :dbcommand:`flushRouterConfig` is available on both :binary:`~bin.mongos` and :binary:`~bin.mongod` instances, and has the following syntax:

- Flush the cache for a specified collection when passed in a
collection namespace parameter:

```javascript
  db.adminCommand(
     { 
       flushRouterConfig: "<db.collection>" 
     } 
  )
```

- Flush the cache for a specified database and all of its collections
when passed in a database namespace parameter:

```javascript
  db.adminCommand(
     { 
       flushRouterConfig: "<db>" 
     } 
  ) 
```

- Flush the cache for all databases and their collections when run
without a parameter or passed in a non-string scalar value (e.g. `1`):

```javascript
  db.adminCommand("flushRouterConfig")
  db.adminCommand( 
     { 
       flushRouterConfig: 1 
     } 
  )
```
