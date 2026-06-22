---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/flushRouterConfig.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
