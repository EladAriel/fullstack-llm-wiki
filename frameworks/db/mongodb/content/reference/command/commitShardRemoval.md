---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/commitShardRemoval.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# commitShardRemoval (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** .. include:: /includes/edit-shards-atlas-compatibility.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( { 
     commitShardRemoval: <shard> 
} )
```

## Behavior

### Access Requirements

.. include:: /includes/removeShard-access-requirements.rst

### Database Migration Requirements

Each database in a sharded cluster has a primary shard. If the shard you want to drain is also the primary of one of the cluster's databases, then you must manually move the databases from its primary shard to a new shard after migrating all data from the shard.

If there is a database that uses the shard you want to use as a primary, the `commitShardRemoval` command returns an error.

For details, see the :dbcommand:`movePrimary` command and the `remove-shards-from-cluster-tutorial` for more information.

### Collection Migration Requirements

Unsharded collections are stored on individual shards. If one of these collections is on the shard you want to remove, you must first migrate the collection to a different shard.

If there is an unsharded collection stored on the shard you want to remove, the `commitShardRemoval` command returns an error.

To migrate an unsharded collection, see the :dbcommand:`moveCollection` command.

## Examples

To start draining a shard, use the :method:`db.adminCommand` method to run the :dbcommand:`startShardDraining` command:

```javascript
db.adminCommand( { startShardDraining: "shard04" } )
```

To check the status of the draining operation, use the :dbcommand:`shardDrainingStatus` command:

If the output shows any databases in the `dbsToMove` field, use the :dbcommand:`movePrimary` command to move them onto a different shard.

If the output shows any unsharded collections in the `collectionsToMove` field, use the :dbcommand:`moveCollection` command to move them onto a different shard.

When :dbcommand:`shardDrainingStatus` shows `{ state: "drainingComplete" }`, the balancer has finished moving chunks off the shard. You can now remove the shard:

## Learn More

- :dbcommand:`startShardDraining`
- :dbcommand:`stopShardDraining`
- :dbcommand:`shardDrainingStatus`
