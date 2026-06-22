---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/mergeChunks.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# mergeChunks (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     mergeChunks: <namespace>,
     bounds : [ 
       { <shardKeyField>: <minFieldValue> },
       { <shardKeyField>: <maxFieldValue> } 
     ] 
   } 
)
```

For compound shard keys, you must include the full shard key in the `bounds` specification. For example, if the shard key is `{ x: 1, y: 1 }`, :dbcommand:`mergeChunks` has the following form:

```javascript
db.adminCommand( 
   { 
     mergeChunks: <namespace>,
     bounds: [ 
       { x: <minValue>, y: <minValue> },
       { x: <maxValue>, y: <maxValue> } 
     ] 
   } 
 )
```

## Command Fields

The command takes the following fields:

## Access Control

On deployments running with :setting:`~security.authorization`, the built-in role :authrole:`clusterManager` provides the required privileges.

## Behavior

> **Note:** Use the :dbcommand:`mergeChunks` only in special circumstances. For
instance, when cleaning up your `sharded cluster` after removing
many documents.

In order to successfully merge chunks, the following must be true:

- In the `bounds` field, `<minkey>` and `<maxkey>` must correspond to
the lower and upper bounds of the `chunks <chunk>` to merge.

- The chunks must reside on the same shard.
- The chunks must be contiguous.
:dbcommand:`mergeChunks` returns an error if these conditions are not satisfied.

## Return Messages

On success, :dbcommand:`mergeChunks` returns this document:

```javascript
{
  "ok" : 1,
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510767081, 1),
     "signature" : {
         "hash" : BinData(0,"okKHD0QuzcpbVQg7mP2YFw6lM04="),
         "keyId" : Long("6488693018630029321")
      }
  },
  "operationTime" : Timestamp(1510767081, 1)
}
```

### Another Operation in Progress

:dbcommand:`mergeChunks` returns the following error message if another metadata operation is in progress on the `config.chunks` collection:

```none
errmsg: "The collection's metadata lock is already taken."
```

If another process, such as balancer process, changes metadata while :dbcommand:`mergeChunks` is running, you may see this error. You can retry the :dbcommand:`mergeChunks` operation without side effects.

### Chunks on Different Shards

If the input `chunks <chunk>` are not on the same `shard`, :dbcommand:`mergeChunks` returns an error similar to the following:

```javascript
{
  "ok" : 0,
  "errmsg" : "could not merge chunks, collection test.users does not contain a chunk ending at { username: \"user63169\" }",
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510767081, 1),
     "signature" : {
         "hash" : BinData(0,"okKHD0QuzcpbVQg7mP2YFw6lM04="),
         "keyId" : Long("6488693018630029321")
      }
  },
  "operationTime" : Timestamp(1510767081, 1)
}
```

### Noncontiguous Chunks

If the input `chunks <chunk>` are not contiguous, :dbcommand:`mergeChunks` returns an error similar to the following:

```javascript
{
  "ok" : 0,
  "errmsg" : "could not merge chunks, collection test.users has more than 2 chunks between [{ username: \"user29937\" }, { username: \"user49877\" })"
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510767081, 1),
     "signature" : {
         "hash" : BinData(0,"okKHD0QuzcpbVQg7mP2YFw6lM04="),
         "keyId" : Long("6488693018630029321")
      }
  },
  "operationTime" : Timestamp(1510767081, 1)

}
```
