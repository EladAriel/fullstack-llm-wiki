---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setDefaultRWConcern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# setDefaultRWConcern (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
  {
    setDefaultRWConcern : 1,
    defaultReadConcern: { <read concern> },
    defaultWriteConcern: { <write concern> },
    writeConcern: { <write concern> },
    comment: <any>
  }
)
```

## Command Fields

The command takes the following fields:

:dbcommand:`setDefaultRWConcern` returns an object that contains the currently configured global default read and write concern. See :dbcommand:`getDefaultRWConcern` for more complete documentation on the returned fields.

## Behavior

> **Note:** Each :binary:`~bin.mongod` in the replica set or sharded cluster
must have `featureCompatibilityVersion <set-fcv>` set to
at least `4.4` to use :dbcommand:`setDefaultRWConcern`.

.. include:: /includes/5.0-cluster-wide-write-concern.rst

MongoDB only applies the global default read or write concern to operations which do not explicitly specify a read or write concern.

If MongoDB applies the global default read or write concern to an operation, that operation behaves as if that read or write concern were explicitly specified by the issuing client.

### Replica Sets

Issue :dbcommand:`setDefaultRWConcern` against the replica set `primary`. The primary replicates the new global default settings to the remaining members of the replica set. Secondaries which have not yet replicated the updated global default settings continue using their local 'stale' copy of the defaults.

Issue the :dbcommand:`setDefaultRWConcern` command with a `writeConcern <setDefaultRWConcern-cmd-writeConcern>` of :writeconcern:`w : "majority" <"majority">` to ensure the command only returns after the changes have propagated to a majority of replica set members.

### Sharded Clusters

Issue the :dbcommand:`setDefaultRWConcern` against a :binary:`~bin.mongos` in the cluster. The :binary:`~bin.mongos` persists the updated settings to the `config server replica set (CSRS) <sharding-config-server>`. Each :binary:`~bin.mongos` periodically issues a :dbcommand:`getDefaultRWConcern` against the CSRS to refresh their local copy of the global settings. A :binary:`~bin.mongos` uses its local 'stale' copy of the global defaults during the time period between refreshes.

> **Warning:** If you are :ref:`converting a replica set to a sharded cluster
<manual-convert-replica-set-to-sharded-cluster>`, you can't run the
`setDefaultRWConcern` command until the conversion completes.

Issue the :dbcommand:`setDefaultRWConcern` command with a `writeConcern <setDefaultRWConcern-cmd-writeConcern>` of :writeconcern:`w : "majority" <"majority">` to ensure the command only returns after the changes have propagated to a majority of CSRS members.

When an application issues an operation against the :binary:`~bin.mongos` without explicitly specifying a read or write concern setting, the :binary:`~bin.mongos` applies the corresponding global default setting.

The global default settings do not propagate to the individual shards. You cannot run :dbcommand:`setDefaultRWConcern` against a shard.

> **Important:** :dbcommand:`setDefaultRWConcern` requires
`featureCompatibilityVersion <set-fcv>` `4.4+`. If you
downgrade your deployment's :ref:`featureCompatibilityVersion
<set-fcv>` from `4.4` to `4.2`, all cluster-wide read and write
concern defaults are lost, but :binary:`~bin.mongos` instances may
continue applying the defaults for up to 30 seconds.

Sharding Administrative Commands Override Write Concern Settings ````````````````````````````````````````````````````````````````

Sharding administrative commands that perform write operations on the `config server <sharding-config-server>`, such as the :dbcommand:`enableSharding` or :dbcommand:`addShard` commands, have specific behavior with global default write concern settings:

- The commands use :writeconcern:`"majority"` regardless of the
configured global default write concern.

- The commands use a minimum `wtimeout <wc-wtimeout>` of `60000`.
The commands only use the global default write concern `wtimeout` if it is greater than `60000`.

### Access Control

For replica sets or sharded clusters enforcing `authentication`, :dbcommand:`setDefaultRWConcern` requires that the authenticated user have the :authaction:`setDefaultRWConcern` privilege action.

The :authrole:`clusterManager` built-in role provides the required privileges to run :dbcommand:`setDefaultRWConcern`.

## Example

### Set Global Default Write Concern

The following operation sets the global write concern to the following:

- :writeconcern:`w: 2 <\<number\>>`
```javascript
db.adminCommand({
  "setDefaultRWConcern" : 1,
  "defaultWriteConcern" : {
    "w" : 2
  }
})
```

The operation returns a document similar to the following:

```javascript
{
  "defaultWriteConcern" : {
   "w" : 2
  },
  "updateOpTime" : Timestamp(1586290895, 1),
  "updateWallClockTime" : ISODate("2020-04-07T20:21:41.849Z"),
  "localUpdateWallClockTime" : ISODate("2020-04-07T20:21:41.862Z"),
  "ok" : 1,
  "$clusterTime" : { ... }
  "operationTime" : Timestamp(1586290925, 1)
}
```

### Set Global Default Read Concern

The following operation sets the global read concern to :readconcern:`"majority"`:

```javascript
db.adminCommand({
  "setDefaultRWConcern" : 1,
  "defaultReadConcern" : { "level" : "majority" }
})
```

The operation returns a document similar to the following:

```javascript
{
  "defaultReadConcern" : {
    "level" : "majority"
  },
  "updateOpTime" : Timestamp(1586290895, 1),
  "updateWallClockTime" : ISODate("2020-04-07T20:21:41.849Z"),
  "localUpdateWallClockTime" : ISODate("2020-04-07T20:21:41.862Z"),
  "ok" : 1,
  "$clusterTime" : { ... }
  "operationTime" : Timestamp(1586290925, 1)
}
```

### Set Global Default Read and Write Concern

The following operation sets the global default read and write concern to the following:

- :writeconcern:`w: 2 <\<number\>>` write concern
- :readconcern:`level: "majority" <"majority">` read concern.
```javascript
db.adminCommand({
  "setDefaultRWConcern" : 1,
  "defaultWriteConcern" : {
    "w" : 2
  },
  "defaultReadConcern" : { "level" : "majority" }
})
```

The operation returns a document similar to the following:

```javascript
"defaultWriteConcern" : {
  "w" : 2
},
"defaultReadConcern" : {
  "level" : "majority"
}
```

### Unset Global Default Read and Write Concern

You can:

- Unset the global default read concern.
- Only unset the global default write concern if you haven't already
set it.

For example, assume the global default read concern is set to :readconcern:`level: "majority" <"majority">`. To unset the global default read concern, use an empty document `{}`:

```javascript
db.adminCommand( {
   "setDefaultRWConcern" : 1, 
   "defaultReadConcern" : {}
} )
```

The operation returns a document that indicates the operation was successful:

```javascript
{
   defaultReadConcern: { level: 'local' },
   defaultWriteConcern: { w: 2, wtimeout: 0 },
   updateOpTime: Timestamp({ t: 1656696934, i: 1 }),
   updateWallClockTime: ISODate("2022-07-01T17:35:40.578Z"),
   defaultWriteConcernSource: 'global',
   defaultReadConcernSource: 'implicit',
   localUpdateWallClockTime: ISODate("2022-07-01T17:35:40.578Z"),
   ok: 1,
   '$clusterTime': {
      ...
   },
   operationTime: Timestamp({ t: 1656632593, i: 1 })
}
```

You can only unset the global default write concern if you haven't already set it.

To unset the global default write concern, use an empty document `{}`:

```javascript
db.adminCommand( {
   "setDefaultRWConcern" : 1, 
   "defaultWriteConcern" : {}
} )
```

If the global default write concern is:

- Unset, the operation succeeds.
- Already set, the operation returns the following error.
```javascript
MongoServerError: The global default write concern cannot be unset
once it is set.
```
