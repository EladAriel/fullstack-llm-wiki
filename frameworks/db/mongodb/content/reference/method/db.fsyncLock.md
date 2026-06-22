---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.fsyncLock.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# db.fsyncLock() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

.. include:: /includes/extracts/wt-fsync-lock-compatibility.rst

### Fsync Locks after Failures

Fsync locks execute on the primary in a replica set or sharded cluster.

If the primary goes down or becomes unreachable due to network issues, the cluster `elects <replica-set-elections>` a new primary from the available secondaries. If a primary with an fsync lock goes down, the new primary does **not** retain the fsync lock and can handle write operations. When elections occur during backup operations, the resulting backup may be inconsistent or unusable.

To recover from the primary going down:

#. Run the :method:`db.fsyncUnlock` method until the lock count reaches zero to release the lock on all nodes.

#. Issue the :method:`db.fsyncLock` command to reestablish the fsync lock on the cluster.

#. Restart the backup.

Additionally, fsync locks are persistent. When the old primary comes online again, you need to run the :method:`db.fsyncUnlock` command to release the lock on the node.

## Example

The following operation runs :method:`db.fsyncLock()`:

```javascript
db.fsyncLock()
```

The operation returns the following status document that includes the `lockCount`:

```javascript
{
   "info" : "now locked against writes, use db.fsyncUnlock() to unlock",
   "lockCount" : Long(1),
   "seeAlso" : "http://dochub.mongodb.org/core/fsynccommand",
   "ok" : 1
}
```

If you run :method:`db.fsyncLock()` again, the operation increments the `lockCount`:

```javascript
{
   "info" : "now locked against writes, use db.fsyncUnlock() to unlock",
   "lockCount" : Long(2),
   "seeAlso" : "http://dochub.mongodb.org/core/fsynccommand",
   "ok" : 1
}
```

To unlock the instance for writes, you must run :method:`db.fsyncUnlock()` twice to reduce the `lockCount` to 0.
