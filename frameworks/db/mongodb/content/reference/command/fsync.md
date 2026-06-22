---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/fsync.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# fsync (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     fsync: 1,
     lock: <Boolean>,
     fsyncLockAcquisitionTimeout: <integer>,
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

## Considerations

.. include:: /includes/extracts/wt-fsync-lock-compatibility-command.rst

### Impact on Larger Deployments

.. versionadded:: 7.1

When the `fsync` command runs on :program:`mongos`, it performs the fsync operation on the entire cluster. By setting the `lock` field to `true`, it sets a lock on the cluster, preventing additional writes.

To take a usable self-managed backup, before locking a sharded cluster:

- Ensure that no chunk migration, resharding, or DDL operations are active.
- Stop the balancer to prevent additional chunk migrations from starting.
> **Important:** :program:`mongod` uses `journaling <journal>` to improve durability.
Use `a file system or volume/block level snapshot tool <backup-with-journaling>`
to create a backup of the data set and the journal together as a single unit.

### Lock Count

The `fsync` command returns a document includes a `lockCount` field. When run on :program:`mongod`, the count indicates the number of fsync locks set on the server.

When run on a sharded cluster, :program:`mongos` sends the fsync operation to each shard and returns the results, which includes the `lockCount` for each.

> **Note:** If the `lockCount` field is greater than zero, all writes
are blocked on the server and cluster. To reduce the lock
count, use the :dbcommand:`fsyncUnlock` command.

### Fsync Locks after Failures

Fsync locks execute on the primary in a replica set or sharded cluster.

If the primary goes down or becomes unreachable due to network issues, the cluster `elects <replica-set-elections>` a new primary from the available secondaries. If a primary with an fsync lock goes down, the new primary does **not** retain the fsync lock and can handle write operations. When elections occur during backup operations, the resulting backup may be inconsistent or unusable.

To recover from the primary going down:

#. Run the :dbcommand:`fsyncUnlock` command until the lock count reaches zero to release the lock on all nodes.

#. Issue the :dbcommand:`fsync` command to reestablish the fsync lock on the cluster.

#. Restart the backup.

Additionally, fsync locks are persistent. When the old primary comes online again, you need to use the :dbcommand:`fsyncUnlock` command to release the lock on the node.

## Examples

### Fsync Lock

> **Note:** .. include:: /includes/extracts/wt-fsync-lock-compatibility-command.rst

The `fsync` command can lock an individual :program:`mongod` instance or a sharded cluster through :program:`mongos`. When run with the `lock` field set to `true`, the fsync operation flushes all data to the storage layer and blocks all additional write operations until you unlock the instance or cluster.

To lock the database, use the `fsync` command to set the `lock` field to `true`:

```javascript
db.adminCommand( { fsync: 1, lock: true } )
```

The operation returns a document that includes the status of the operation and the `lockCount`:

```javascript
{
   "info" : "now locked against writes, use db.fsyncUnlock() to unlock",
   "lockCount" : Long(1),
   "seeAlso" : "http://dochub.mongodb.org/core/fsynccommand",
   "ok" : 1
}
```

When locked, write operations are blocked. Separate connections may continue read operations until the first attempt at a write operation, then they also wait until the sever or cluster is unlocked.

> **Important:** The fsync lock operation maintains a lock count.
To unlock a server or cluster for writes, the lock count
must be zero. That is, for the given number of times you perform an fsync
lock, you must issue a corresponding number of unlock operations to unlock
the server or cluster for writes.

### Fsync Unlock

To unlock a server of cluster, use the :dbcommand:`fsyncUnlock` command:

```javascript
db.adminCommand( { fsyncUnlock: 1 } )
```

Repeat this command as many times as needed to reduce the lock count to zero. Once the lock count reaches zero, the server or cluster can resume writes.

### Check Lock Status

To check the state of the fsync lock, use :method:`db.currentOp()`. Use the following JavaScript function in the shell to test if the server or cluster is currently locked:

```javascript
serverIsLocked = function () {
                     var co = db.currentOp();
                     if (co && co.fsyncLock) {
                         return true;
                     }
                     return false;
                 }
```

After loading this function into your :binary:`~bin.mongosh` session, call it with the following syntax:

```javascript
serverIsLocked()
```

This function will return `true` if the server or cluster is currently locked and `false` if the server or cluster is not locked.
