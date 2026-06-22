---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetResizeOplog.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# replSetResizeOplog (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

> **Note:** To resize the oplog in Atlas, see `set-oplog-min-window`.

## Syntax

The command has the following form:

```javascript
db.adminCommand(
   { 
     replSetResizeOplog: <int>, 
     size: <double>, 
     minRetentionHours: <double>
   }
 )
```

## Command Fields

The command takes the following fields:

> **Seealso:** - :option:`--oplogSize <mongod --oplogSize>` / :setting:`replication.oplogSizeMB`
- :option:`--oplogMinRetentionHours <mongod --oplogMinRetentionHours>` / :setting:`storage.oplogMinRetentionHours`

## Behavior

You can use `replSetResizeOplog` on :binary:`~bin.mongod` instances running with the `Wired Tiger storage engine <storage-wiredtiger>` or the `in-memory storage engine <storage-inmemory>`.

See the `tutorial-change-oplog-size` tutorial for a procedure on using `replSetResizeOplog` command to resize the oplog.

.. include:: /includes/fact-oplog-size.rst

You cannot drop the `local.oplog.rs` collection. For more information on this restriction, see `oplog-coll-behavior`.

`replSetResizeOplog` overrides the maximum oplog size or minimum oplog retention period set at startup by:

- :setting:`replication.oplogSizeMB` / :option:`--oplogSizeMB <mongod
--oplogSize>`, and

- :setting:`storage.oplogMinRetentionHours` /
:option:`--oplogMinRetentionHours <mongod --oplogMinRetentionHours>` respectively.

The new oplog size persists after a server restart, unless you use:

- :setting:`storage.oplogMinRetentionHours`, or
- :option:`--oplogMinRetentionHours <mongod --oplogMinRetentionHours>`.
> **Important:** Reducing the maximum oplog size results in truncation of the oldest
oplog entries until the oplog reaches the new configured size.
Similarly, reducing the minimum oplog retention period
results in truncation of oplog entries older that the specified
period if the oplog has exceeded the maximum configured size.
Oplog truncation due to reduced oplog size or retention period can
result in unexpected behavior from clients still reading those oplog
entries, including:
- Open `change streams <changeStreams>` may become
  invalidated
- Secondaries which have not replicated those oplog entries
  may require `resynchronization <replica-set-initial-sync>`.
- Backups using :binary:`~bin.mongodump` with
  :option:`--oplog <mongodump.--oplog>` against the member may
  not capture entries prior to truncation.

### Minimum Oplog Retention Period

A :binary:`~bin.mongod` has the following behavior when configured with a minimum oplog retention period:

- The oplog can grow without constraint so as to retain oplog entries
for the configured number of hours. This may result in reduction or exhaustion of system disk space due to a combination of high write volume and large retention period.

- If the oplog grows beyond its maximum size, the :binary:`~bin.mongod`
may continue to hold that disk space even if the oplog returns to its maximum size or is configured for a smaller maximum size. See `replSetResizeOplog-cmd-compact`.

- The :binary:`~bin.mongod` compares the system wall clock to an
oplog entry creation `wall clock time` when enforcing oplog entry retention. Clock drift between cluster components may result in unexpected oplog retention behavior. See `production-notes-clock-synchronization` for more information on clock synchronization across cluster members.

### `replSetResizeOplog` Does Not Replicate To Other Members

Changing the oplog size or minimum oplog retention period of a given replica set member with `replSetResizeOplog` does not change the oplog size of any other member in the replica set. You must run `replSetResizeOplog` on each replica set member in your cluster to change the oplog size or minimum retention period for all members.

### Reducing Oplog Size Does Not Immediately Return Disk Space

Reducing the oplog size does not immediately reclaim that disk space. This includes oplog size reduction due to truncation of oplog events older than of the `minimum oplog retention period <replSetResizeOplog-cmd-minimum-retention>`.

To immediately free unused disk space after reducing the oplog size, run :dbcommand:`compact` against the `oplog.rs` collection in the `local` database during a maintenance period. `compact` blocks all operations on the database it runs against. Running `compact` against `oplog.rs` therefore prevents oplog synchronization. For a procedure on resizing the oplog and compacting `oplog.rs`, see `/tutorial/change-oplog-size`.

### Resource Locking

`replSetResizeOplog` takes an exclusive (W) lock on the `oplog <local.oplog.rs>` and blocks other operations on the collection until it finishes.

For more information on locking in MongoDB, see `/faq/concurrency`.

## Examples

### Change the Maximum Oplog Size

Use the :method:`db.collection.stats()` :binary:`~bin.mongosh` method to display the current maximum oplog size, `maxSize`, in megabytes. For example:

```javascript
db.getSiblingDB("local").oplog.rs.stats(1024*1024).maxSize
```

The above command returns the oplog size of this member in megabytes:

```javascript
990
```

The following command uses `replSetResizeOplog` to change the oplog size of this member to 16384 megabytes:

```javascript
db.adminCommand({ "replSetResizeOplog": 1, size: Double(16384)})
```

To verify the new oplog size, rerun the :method:`db.collection.stats()` method:

```javascript
db.getSiblingDB("local").oplog.rs.stats(1024*1024).maxSize
```

The above command returns:

```javascript
"maxSize": Long("16834")
```

> **Warning:** Reducing the size of the oplog in a node removes data from it. This
may cause replica members syncing with that node to become stale.
To resync those members, see `/tutorial/resync-replica-set-member`.

### Change the Minimum Oplog Retention Period

1. Connect :binary:`~bin.mongosh` to the :binary:`~bin.mongod`
replica set member.

#. Optional. Use the :method:`db.serverStatus()` command to verify the current minimum oplog retention value as :serverstatus:`oplogTruncation.oplogMinRetentionHours`:

```javascript
   db.getSiblingDB("admin").serverStatus().oplogTruncation.oplogMinRetentionHours

The command returns the currently configured minimum oplog retention
period for the :binary:`~bin.mongod`. For example:

.. code-block:: javascript

   1.5

If the :binary:`~bin.mongod` has no minimum oplog retention period,
the operation returns an empty result.
```

#. Use the `replSetResizeOplog` command to modify the configured minimum oplog retention period. For example, the following sets the minimum oplog retention period to `2` hours:

```javascript
   db.adminCommand({
     "replSetResizeOplog" : 1, 
     "minRetentionHours" : 2
   })
```
