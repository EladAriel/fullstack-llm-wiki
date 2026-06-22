---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/compact.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# compact (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     compact: <string>, 
     dryRun: <boolean>,
     force: <boolean>, // Optional
     freeSpaceTargetMB: <int>, // Optional 
     comment: <any>, // Optional
   }
)
```

## Command Fields

The command takes the following fields:

> **Note:** The `compact` command does not block `crud` operations
on the database it is compacting.

## `compact` Required Privileges

For clusters enforcing `authentication <authentication>`, you must authenticate as a user with the :authaction:`compact` privilege action on the target collection. The :authrole:`dbAdmin` and :authrole:`hostManager` roles provide the required privileges for running `compact` against non-system collections.

For `system collections <metadata-system-collections>`, you must:

1. Create a custom role that grants the `compact` action on
the system collection.

2. Grant that role to a new or existing user.
3. Authenticate as that user to perform the `compact`
command.

For example, the following operations create a custom role that grants the `compact` action against the specified database and collection:

```javascript
use admin
db.createRole(
  {
    role: "myCustomCompactRole",
    privileges: [
      {
        resource: { "db" : "<database>" , "collection" : "<collection>" },
        actions: [ "compact" ]
      }
    ],
    roles: []
  }
)
```

For more information on configuring the `resource` document, see `resource-document`.

To add the :authrole:`dbAdmin`, :authrole:`hostManager`, or the custom role to an existing user, use :method:`db.grantRolesToUser` or :method:`db.updateUser()`. The following operation grants the custom `compact` role to the `myCompactUser` on the `admin` database:

```javascript
use admin
db.grantRolesToUser("myCompactUser", [ "dbAdmin" | "myCustomCompactRole" ] )
```

To add the :authrole:`dbAdmin` or the custom role to a new user, specify the role to the `roles` array of the :method:`db.createUser()` method when creating the user.

```javascript
use admin
db.createUser(
  { 
     user: "myCompactUser",
     pwd: "myCompactUserPassword",
     roles: [
       { role: "dbAdmin", db: "<database>" } | "myCustomCompactRole"
     ]
   }
)
```

## Behavior

### Monitoring Progress

To check the `compact` operation's progress, monitor the :binary:`~bin.mongod` log file or run :method:`db.currentOp()` from another shell instance.

### Operation Termination

If you terminate `compact` with the :method:`db.killOp() <db.killOp()>` method or restart the server before the operation finishes, `compact` ends and may fail its attempt to release disk space back to the operating system.

### Disk Space

The `compact` command attempts to reduce the disk space consumed for data and indexes in a collection by releasing obsolete blocks back to the operating system. The effectiveness of `compact` is relative to how many blocks are available to be released and where in the data file the blocks are.

To see how the storage space changes for the collection, run the :dbcommand:`collStats` command before and after compaction. You can use the output metric `collStats.freeStorageSize` to view the amount of storage available for reuse.

The operation is iterative and operates on segments of the data file in each pass. To view an estimate of how much space `compact` will release, use the `dryRun` flag. Calling `compact` on a collection compacts both the collection and its associated indexes.

`compact` may require additional disk space to run.

### Backups

.. include:: /includes/compaction-checkpoints.rst

Multi-Shard Transactions ````````````````````````

> **Note:** If your deployment uses secondary reads and multi-shard transactions,
consider running an `initial sync <replica-set-initial-sync>` instead of
`compact`.

When `compact` runs, WiredTiger temporarily adjusts its block-manager strategy to accommodate the compact workload. This adjustment can slow checkpoint operations and increase the time that a member takes to commit a transaction. Delayed transaction commits can cause significant read latency, replication lag, and operational queuing.

### Replica Sets

You can use `compact` on collections and indexes that are stored in a replica set, however there are some important considerations:

- The primary node does not replicate the `compact` command to the
secondaries.

- You should run `compact` on secondary nodes whenever possible. If
you cannot run `compact` on secondaries, see the `force <compact-force-option>` option.

- Starting in MongoDB 6.1.0 (and 6.0.2):
- A secondary node can replicate while `compact` is running.
- Reads are permitted.
To run `compact` on a cluster

Version Specific Considerations for Secondary Nodes ```````````````````````````````````````````````````

- A secondary node can replicate while `compact` is running.
- Reads are permitted.
While the `compact` command is running, the replica set remains in a :replstate:`SECONDARY` status.

For more information about replica set member states, see See `replica-set-member-states`.

For replica set maintenance and availability, see `perform-maint-on-replica-set`.

### Sharded Clusters

`compact` only applies to :binary:`~bin.mongod` instances. In a sharded environment, run `compact` on each shard separately as a maintenance operation.

You cannot issue `compact` against a :binary:`~bin.mongos` instance.

### Concurrent Compact Commands Not Allowed

If you try to run multiple concurrent `compact` commands on the same collection, MongoDB returns an error.

## Example

> **Note:** The following examples include `force: true`, which is required
when running `compact` against an active replica set primary.
To run `compact` without `force: true`, step down the primary
first. For more information, see `compact-cmd-replica-sets`.

### Compact a Collection

The following operation runs the `compact` command on the `movies` collection:

### Estimate Compaction

The following operation performs a dry run of the `compact` command on the `movies` collection:

## Learn More

- :dbcommand:`autoCompact`
