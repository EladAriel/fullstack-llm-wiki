---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/startShardDraining.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# startShardDraining (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** .. include:: /includes/edit-shards-atlas-compatibility.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( { 
     startShardDraining: <shardToDrain> 
} )
```

## Behavior

### Access Requirements

.. include:: /includes/removeShard-access-requirements.rst

### No Cluster Back Ups During Shard Drain

You cannot back up the cluster while draining the shard.

### Concurrent Drain Shard Operations

You can have more than one shard draining operation in progress at a time.

### Database Migration Requirements

.. include:: /includes/sharding-database-migration-requirements.rst

### Collection Migration Requirements

.. include:: /includes/sharding-collection-migration-requirements.rst

### Chunk Balancing

When you drain a shard in a cluster with an uneven chunk distribution, the balancer first removes the chunks from the draining shard and then balances the remaining uneven chunk distribution.

> **Seealso:** :dbcommand:`balancerCollectionStatus`

### Write Concern

:program:`mongos` converts the `write concern <write-concern>` of the `startShardDraining` command to :writeconcern:`"majority"`.

### Change Streams

Draining a shard may cause an open `change stream cursor <changeStreams>` to close, and the closed change stream cursor may not be fully resumable.

### DDL Operations

If you run `startShardDraining` while your cluster is executing a DDL operation (operation that modifies a collection such as :dbcommand:`reshardCollection`), the shard draining only executes after the concurrent DDL operation finishes.

## Examples

To start draining a shard, use the :method:`db.adminCommand` method:

```javascript
db.adminCommand( {
   startShardDraining: "shard04"
} )
```

## Learn More

- `remove-shards-from-cluster-tutorial`
- :dbcommand:`shardDrainingStatus`
- :dbcommand:`commitShardRemoval`
- :dbcommand:`stopShardDraining`
