---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/enableSharding.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# enableSharding (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

- Recommended.  Specify the database to create:
```javascript
  db.adminCommand( 
     { 
       enableSharding: "<database name>"
     } 
  )
```

- Optionally, you can include the primary shard specification in the command,
although this is not recommended:

```javascript
  db.adminCommand( 
     { 
       enableSharding: "<database name>",
       primaryShard: "<shard name>"  
     } 
  )
```

You can only run the :dbcommand:`enableSharding` command on the `admin` database from a :binary:`~bin.mongos` instance.

## Command Fields

The command takes the following fields:

### Returns

The command returns a document that contains status of the operation.

## Behavior

### Write Concern

.. include:: /includes/extracts/mongos-operations-wc-enable-sharding.rst

### Primary Shard

In general, you should not need to specify the `primaryShard <cmd-enableSharding-primaryShard>` in the command. Instead, allow the balancer to select the primary shard.

However, if you do specify the `primaryShard <cmd-enableSharding-primaryShard>` in the command for a `database <cmd-enableSharding-db>` and the database is already sharding enabled with a different primary shard, the operation returns an error and the primary shard for the database remains as before. To change the primary shard for a database, use :dbcommand:`movePrimary` instead.

## Example

The following command, run from a :binary:`~bin.mongos`, creates the the `shardTest` database:

```javascript
db.adminCommand( { enableSharding: "shardTest" } )
```

> **Seealso:** - `/tutorial/deploy-shard-cluster`
- :method:`sh.shardCollection()`
