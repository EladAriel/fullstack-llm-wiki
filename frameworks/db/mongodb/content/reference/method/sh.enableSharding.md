---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.enableSharding.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# sh.enableSharding() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`sh.enableSharding` has the following form:

```javascript
sh.enableSharding( 
   <database>,
   <primary shard>  // Optional. 
)
```

### Parameter

The :method:`sh.enableSharding()` method takes the following parameter:

## Behavior

### Write Concern

.. include:: /includes/extracts/mongos-operations-wc-enable-sharding.rst

### Primary Shard

In general, you should not need to specify the `primaryShard <method-enableSharding-primaryShard>` in the command. Instead, allow the balancer to select the primary shard.

However, if you do specify the `primary shard <method-enableSharding-primaryShard>` for a database and the database is already enabled for sharding with a different primary shard, the operation returns an error and the primary shard for the database remains as before. To change the primary shard for a database, use the :dbcommand:`movePrimary` command instead.

## Example

The following example, run from a :binary:`~bin.mongos`, explicitly creates the `shardTest` database:

```javascript
sh.enableSharding("shardTest")
```

To verify, run :method:`sh.status()`.

> **Seealso:** - :method:`sh.shardCollection()`
- `/tutorial/deploy-shard-cluster`
