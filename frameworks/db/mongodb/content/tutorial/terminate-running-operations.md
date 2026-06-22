---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/terminate-running-operations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# Terminate Running Operations

## Overview

MongoDB provides two facilitates to terminate running operations: :method:`~cursor.maxTimeMS()` and :method:`db.killOp()`. Use these operations as needed to control the behavior of operations in a MongoDB deployment.

## Available Procedures

### `maxTimeMS`

The :method:`~cursor.maxTimeMS()` method sets a time limit for an operation. When the operation reaches the specified time limit, MongoDB interrupts the operation at the next `interrupt point`.

Terminate a Query `````````````````

From :binary:`~bin.mongosh`, use the following method to set a time limit of 30 milliseconds for this query:

```javascript
db.location.find( { "town": { "$regex": "(Pine Lumber)",
                              "$options": 'i' } } ).maxTimeMS(30)
```

Terminate a Command ```````````````````

Consider a potentially long running operation using :dbcommand:`distinct` to return each distinct `collection` field that has a `city` key:

```javascript
db.runCommand( { distinct: "collection",
                 key: "city" } )
```

You can add the `maxTimeMS`  field to the command document to set a time limit of 45 milliseconds for the operation:

```javascript
db.runCommand( { distinct: "collection",
                 key: "city",
                 maxTimeMS: 45 } )
```

Operations that reach `maxTimeMS` will return a `MaxTimeMSExpired` error.

### `killOp`

The :method:`db.killOp()` method interrupts a running operation at the next `interrupt point`. :method:`db.killOp()` identifies the target operation by operation ID.

```javascript
db.killOp(<opId>)
```

.. include:: /includes/extracts/warning-terminating-ops-method.rst

Sharded Cluster ````````````````

The :dbcommand:`killOp` command can be run on a :binary:`~bin.mongos` and can kill queries (i.e. read operations) that span shards in a cluster. The :dbcommand:`killOp` command from the :binary:`~bin.mongos` does not propagate to the shards when the operation to be killed is a write operation.

For more information on killing operations on a sharded cluster, see:

- `kill-read-ops-sharded-cluster`
- `kill-write-ops-sharded-cluster`
For information on how to list sharding operations that are active on a :binary:`~bin.mongos`, see the `localOps` parameter in :pipeline:`$currentOp`.
