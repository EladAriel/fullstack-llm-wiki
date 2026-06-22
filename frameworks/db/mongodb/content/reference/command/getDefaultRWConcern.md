---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getDefaultRWConcern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# getDefaultRWConcern (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following form:

```javascript
   db.adminCommand( 
      { 
        getDefaultRWConcern: 1 , 
        inMemory: <boolean>, 
        comment: <any> 
      } 
   )
```

## Command Fields

The command has the following fields:

## Output

The output may include the following fields:

> **Seealso:** :dbcommand:`setDefaultRWConcern`

## Behavior

> **Note:** Each :binary:`~bin.mongod` in the replica set or sharded cluster
must have `featureCompatibilityVersion <set-fcv>` set to
at least `4.4` to use :dbcommand:`getDefaultRWConcern`.  If you
downgrade your deployment's :ref:`featureCompatibilityVersion
<set-fcv>` from `4.4` to `4.2`, all cluster-wide read and write
concern defaults are lost, but :binary:`~bin.mongos` instances may
continue applying the defaults for up to 30 seconds.

### Replica Sets

You can issue :dbcommand:`getDefaultRWConcern` against any data-bearing member of the replica set (i.e. not against an `arbiter`).

A secondary can return a 'stale' version of the global default settings if it has not yet replicated the latest changes from the primary.

### Sharded Clusters

Issue the :dbcommand:`setDefaultRWConcern` against a :binary:`~bin.mongos` in the cluster.

Each :binary:`~bin.mongos` periodically refreshes its local copy of the global default settings. A :binary:`~bin.mongos` can return a 'stale' version of the global default settings if it has not yet refreshed its local copy after a recent update to the global default settings or if it fetched its settings from a lagged `config server secondary <sharding-config-server>`.

The global default settings do not propagate to the individual shards. You cannot run :dbcommand:`getDefaultRWConcern` against a shard.

### Access Control

For replica sets or sharded clusters enforcing `authentication`, :dbcommand:`getDefaultRWConcern` requires that the authenticated user have the :authaction:`getDefaultRWConcern` privilege action.

The :authrole:`clusterManager` or :authrole:`clusterMonitor` built-in roles provides the required privileges to run :dbcommand:`getDefaultRWConcern`.

## Example

The following operation retrieves the currently configured global default read and write concern for the :binary:`~bin.mongod`.

```javascript
db.adminCommand({
  "getDefaultRWConcern": 1
})
```

The operation returns output similar to the following:

```javascript
{
  "defaultWriteConcern" : {
    "w" : "majority"
  },
  "defaultReadConcern" : {
    "level" : "majority"
  },
  "defaultWriteConcernSource" : "global",
  "defaultReadConcernSource" : "global",
  "updateOpTime" : Timestamp(1586290895, 1),
  "updateWallClockTime" : ISODate("2020-04-07T20:21:41.849Z"),
  "localUpdateWallClockTime" : ISODate("2020-04-07T20:21:41.862Z"),
  "ok" : 1,
  "$clusterTime" : { ... }
  "operationTime" : Timestamp(1586290925, 1)
}
```
