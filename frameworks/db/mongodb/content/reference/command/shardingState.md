---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/shardingState.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# shardingState (database command)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
  { 
    shardingState: 1   
  }
)
```

## Behavior

For :dbcommand:`shardingState` to detect that a :binary:`~bin.mongod` is a member of a sharded cluster, the :binary:`~bin.mongod` must satisfy the following conditions:

#. the :binary:`~bin.mongod` is a primary member of a replica set, and

#. the :binary:`~bin.mongod` instance is a member of a sharded cluster.

If :dbcommand:`shardingState` detects that a :binary:`~bin.mongod` is a member of a sharded cluster, :dbcommand:`shardingState` returns a document that resembles the following prototype:

```javascript
{
  "enabled" : true,
  "configServer" : "<configdb-string>",
  "shardName" : "<string>",
  "shardHost" : "string:",
  "versions" : {
    "<database>.<collection>" : {
      "placementVersion": Timestamp({ t: 1, i: 1024 }),
      "timestamp": Timestamp({ t: 1682444810, i: 8 })
    }, 
    "<database>.<collection>" : {
      "placementVersion": Timestamp({ t: 0, i: 0 }),
      "timestamp": Timestamp({ t: 0, i: 0 })
    } 
  },
  "ok" : 1,
  "$clusterTime" : {
     "clusterTime" : Timestamp({ t: 1682457265, i: 1 }),
     "signature" : {
        "hash" : BinData(0,"B2ViX7XLzFLS5Fl9XEuFXbwKIM4="),
        "keyId" : Long("6488045157173166092")
     }
  },
  "operationTime" : Timestamp({ t: 1682457260, i: 1 })
}
```

Otherwise, :dbcommand:`shardingState` will return the following document:

```javascript
{
  "enabled" : false,
  "ok" : 1,
  "$clusterTime" : {
     "clusterTime" : Timestamp({t:1510716515, i: 1}),
     "signature" : {
        "hash" : BinData(0,"B2ViX7XLzFLS5Fl9XEuFXbwKIM4="),
        "keyId" : Long("6488045157173166092")
     }
  },
  "operationTime" : Timestamp({t: 1510716515, i: 1})
}
```

The response from :dbcommand:`shardingState` when used with a `config server <config database>` is:

```javascript
{
   "enabled" : false,
   "ok" : 1,
   "operationTime" : Timestamp({t: 1510767613, i: 1}),
   "$gleStats" : {
      "lastOpTime" : Timestamp({t: 0, i: 0}),
      "electionId" : ObjectId("7fffffff0000000000000001")
   },
   "$clusterTime" : {
      "clusterTime" : Timestamp({t: 1510767613, i: 1}),
      "signature" : {
         "hash" : BinData(0,"IwBZ4SZjIMI5NdM62NObV/R31GM="),
         "keyId" : Long("6488693018630029321")
      }
   }
}
```

> **Note:** :binary:`~bin.mongos` instances do not provide the
:dbcommand:`shardingState`.

> **Warning:** This command obtains a write lock on the affected database and
will block other operations until it has completed; however, the
operation is typically short lived.
