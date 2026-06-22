---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/change-oplog-size.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Change the Oplog Size of Self-Managed Replica Set Members

> **Warning:** You cannot drop the `local.oplog.rs` collection. For more information on
this restriction, see `oplog-coll-behavior`.

This procedure changes the size of the oplog [#oplog]_ on each member of a replica set using the :dbcommand:`replSetResizeOplog` command, starting with the `secondary` members before proceeding to the `primary`.

Perform these steps on each `secondary` replica set member first. Once you have changed the oplog size for all secondary members, perform these steps on the `primary`.

## A. Connect to the replica set member

Connect to the replica set member using :binary:`~bin.mongosh`:

```bash
mongosh --host <hostname>:<port>
```

> **Note:** If the replica set enforces `authentication <authentication>`,
you must authenticate as a user with privileges to modify the
`local` database, such as the :authrole:`clusterManager` or
:authrole:`clusterAdmin` role.

## B. (Optional) Verify the current size of the oplog

To view the current size of the oplog, switch to the `local` database and run :method:`db.collection.stats()` against the `oplog.rs` collection. :method:`~db.collection.stats()` displays the oplog size as `collStats.maxSize`.

```javascript
use local
db.oplog.rs.stats().maxSize
```

The `maxSize` field displays the collection size in bytes.

## C. Change the oplog size of the replica set member

Resize the oplog with the :dbcommand:`replSetResizeOplog` command. The `size` is a double and must be greater than `990` megabytes. To explicitly cast the oplog `size` in :binary:`~bin.mongosh`, use the `Double()` constructor.

The following operation changes the oplog size of the replica set member to 16 gigabytes, or 16000 megabytes.

```javascript
db.adminCommand({replSetResizeOplog: 1, size: Double(16000)})
```

.. include:: /includes/fact-oplog-size.rst

## D. (Optional) Compact `oplog.rs` to reclaim disk space

Reducing the size of the oplog does not automatically reclaim the disk space allocated to the original oplog size. You must run :dbcommand:`compact` against the `oplog.rs` collection in the `local` database to reclaim disk space. There are no benefits to running `compact` on the `oplog.rs` collection after increasing the oplog size.

> **Important:** A replica set member cannot replicate oplog entries when a
`compact` operation is ongoing on `oplog.rs` because
it prevents oplog synchronization. You must schedule `compact`
operations on the oplog during a maintenance window. Oplog
replication cannot occur during that time window.

Do **not** run `compact` against the primary replica set member. Connect a :binary:`mongo <bin.mongo>` shell directly to the primary (not the replica set) and run :method:`rs.stepDown()`. If successful, the primary steps down. From the :binary:`mongo <bin.mongo>` shell, run the `compact` command on the now-secondary member.

The following operation runs the `compact` command against the `oplog.rs` collection:

```javascript
use local
db.runCommand({ "compact" : "oplog.rs" } )
```

For clusters enforcing `authentication <authentication>`, authenticate as a user with the :authaction:`compact` privilege action on the `local` database and the `oplog.rs` collection. For complete documentation on :dbcommand:`compact` authentication requirements, see `compact-authentication`.
