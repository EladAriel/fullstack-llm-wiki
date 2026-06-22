---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/removeShard.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# removeShard (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** .. include:: /includes/edit-shards-atlas-compatibility.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     removeShard : <shardToRemove> 
   } 
)
```

## Behavior

### No Cluster Back Ups During Shard Removal

You cannot back up the cluster data during shard removal.

### Concurrent `removeShard` Operations

You can have more than one :dbcommand:`removeShard` operation in progress.

### Access Requirements

If you have :setting:`~security.authorization` enabled, you must have the :authrole:`clusterManager` role or any role that includes the :authaction:`removeShard` action.

### Database Migration Requirements

Each database in a sharded cluster has a primary shard. If the shard you want to remove is also the primary of one of the cluster's databases, then you must manually move the databases to a new shard after migrating all data from the shard. See the :dbcommand:`movePrimary` command and the `/tutorial/remove-shards-from-cluster` for more information.

### Chunk Balancing

.. include:: /includes/fact-remove-shard-balance-order.rst

> **Seealso:** :dbcommand:`balancerCollectionStatus`

### Write Concern

.. include:: /includes/extracts/mongos-operations-wc-remove-shard.rst

### Change Streams

.. include:: /includes/extracts/changestream-remove-shard-with-link.rst

### DDL Operations

If you run `removeShard` while your cluster executes a DDL operation (operation that modifies a collection such as :dbcommand:`reshardCollection`), `removeShard` only executes after the concurrent DDL operation finishes.

## Example

From :binary:`~bin.mongosh`, the :dbcommand:`removeShard` operation resembles the following:

```javascript
db.adminCommand( { removeShard : "bristol01" } )
```

Replace `bristol01` with the name of the shard to remove. When you run :dbcommand:`removeShard`, the command returns with a message that resembles the following:

```javascript
{
   "msg" : "draining started successfully",
   "state" : "started",
   "shard" : "bristol01",
   "note" : "you need to call moveCollection for collectionsToMove and afterwards movePrimary for the dbsToMove", 
   "dbsToMove" : [
      "fizz",
      "buzz"
   ],
   "collectionsToMove" : [
      "fizz.coll1",
      "buzz.coll1"
   ],
   "ok" : 1,
   "operationTime" : Timestamp(1575398919, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575398919, 2),
      "signature" : {
         "hash" : BinData(0,"Oi68poWCFCA7b9kyhIcg+TzaGiA="),
         "keyId" : Long("6766255701040824328")
      }
   }
}
```

The balancer begins migrating ("draining") chunks from the shard named `bristol01` to other shards in the cluster. These migrations happen slowly in order to avoid placing undue load on the cluster.

If you run the command again, :dbcommand:`removeShard` returns the current status of the process. For example, if the operation is in an `ongoing` state, the command returns an output that resembles the following:

```javascript
{
   "msg" : "draining ongoing",
   "state" : "ongoing",
   "remaining" : {
      "chunks" : Long(2),
      "dbs" : Long(2),
      "jumboChunks" : Long(0),
      "collectionsToMove": Long(2)  
   },
   "note" : "you need to call moveCollection for collectionsToMove and afterwards movePrimary for the dbsToMove",
   "dbsToMove" : [
      "fizz",
      "buzz"
   ],
   "collectionsToMove" : [
      "fizz.coll1",
      "buzz.coll1"
   ],
   "ok" : 1,
   "operationTime" : Timestamp(1575399086, 1655),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575399086, 1655),
      "signature" : {
         "hash" : BinData(0,"XBrTmjMMe82fUtVLRm13GBVtRE8="),
         "keyId" : Long("6766255701040824328")
      }
   }
}
```

In the output, the `remaining` field includes the following fields:

Continue checking the status of the :dbcommand:`removeShard` command (i.e. rerun the command) until the number of chunks remaining is `0`.

```javascript
{
   "msg" : "draining ongoing",
   "state" : "ongoing",
   "remaining" : {
      "chunks" : Long(0),             // All chunks have moved
      "dbs" : Long(2),
      "jumboChunks" : Long(0),
      "collectionsToMove": Long(2)       
   },
   "note" : "you need to call moveCollection for collectionsToMove and afterwards movePrimary for the dbsToMove",
   "dbsToMove" : [
      "fizz",
      "buzz"
   ],
   "collectionsToMove" : [
      "fizz.coll1",
      "buzz.coll1"
   ],
   "ok" : 1,
   "operationTime" : Timestamp(1575400343, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575400343, 1),
      "signature" : {
         "hash" : BinData(0,"9plu5B/hw4uWAgEmjjBP3syw1Zk="),
         "keyId" : Long("6766255701040824328")
      }
   }
}
```

After the balancer drains all chunks from the shard, you may need to manually move your collections and databases out of the drained shard.

If the `removeShard` output contains collections in the `collectionsToMove` field, use :dbcommand:`moveCollection` to move those collections to a shard other than the draining shard or drop the collections (which deletes the associated data files).

If the `removeShard` output contains databases in the `dbsToMove` field, use :dbcommand:`movePrimary` for those databases or drop the databases (which deletes the associated data files).

> **Note:** For best performance, move your collections before you move your databases.

After the balancer completes moving all chunks off the shard and you have handled the `dbsToMove` and `collectionsToMove`, :dbcommand:`removeShard` can finish. Running :dbcommand:`removeShard` again returns output that resembles the following:

```javascript
{
   "msg" : "removeshard completed successfully",
   "state" : "completed",
   "shard" : "bristol01",
   "ok" : 1,
   "operationTime" : Timestamp(1575400370, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575400370, 2),
      "signature" : {
         "hash" : BinData(0,"JjSRciHECXDBXo0e5nJv9mdRG8M="),
         "keyId" : Long("6766255701040824328")
      }
   }
}
```
