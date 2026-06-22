---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/build-indexes-on-replica-sets.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# Create a Rolling Index Build on Replica Sets

## About this Task

Rolling index builds are an alternative to `default index builds <index-operations>`.

.. include:: /includes/rolling-index-build-cases.rst

## Considerations

### Unique Indexes

To create `unique indexes <index-type-unique>` using the following procedure, you must stop all writes to the collection during this procedure.

If you cannot stop all writes to the collection during this procedure, do not use the procedure on this page. Instead, build your unique index on the collection by issuing :method:`db.collection.createIndex()` on the primary for a replica set.

### Oplog Size

Ensure that your `oplog` is large enough to permit the indexing or re-indexing operation to complete without falling too far behind to catch up. See the `oplog sizing <replica-set-oplog-sizing>` documentation for additional information.

Rolling index builds lower the resiliency of your cluster and increase build duration.

## Prerequisites

For building unique indexes To create `unique indexes <index-type-unique>` using the following procedure, you must stop all writes to the collection during the index build. Otherwise, you may end up with inconsistent data across the replica set members.

> **Warning:**    If you cannot stop all writes to the collection, do not use the
   following procedure to create unique indexes.

## Procedure

> **Important:** The following procedure to build indexes in a rolling fashion
applies to replica set deployments, and not sharded clusters. For
the procedure for sharded clusters, see
`/tutorial/build-indexes-on-sharded-clusters` instead.

### 1. Hide and Restart One Secondary.

Run the following commands on your primary node to hide the secondary that will build the new index.

In this example, the secondary that will build the new index is the third node in `cfg.members`.

```bash
var cfg = rs.conf();
// Record originalPriority so that you can reset it later.
var originalPriority = cfg.members[2].priority;
cfg.members[2].priority = 0;
cfg.members[2].hidden = 1;
rs.reconfig(cfg);
```

### 2. Stop One Secondary and Restart as a Standalone.

Stop the :binary:`~bin.mongod` process associated with a secondary. Restart after making the following configuration updates:

port, you ensure that the other members of the replica set and all clients will not contact the member while you are building the index.

### 3. Build the Index.

Connect directly to the :binary:`~bin.mongod` instance running as a standalone on the new port and create the new index for this instance.

For example, connect :binary:`~bin.mongosh` to the instance, and use the :method:`~db.collection.createIndex()` to create an ascending index on the `username` field of the `records` collection:

```bash
db.records.createIndex( { username: 1 } )
```

### 4. Restart the Program `mongod` as a Replica Set Member.

When the index build completes, shutdown the :binary:`~bin.mongod` instance. To return the node to its original configuration, undo the configuration changes that you made when you started the node as a standalone. Then, restart the node as a member of the replica set.

> **Important:** Be sure to remove the `disableLogicalSessionCacheRefresh`
parameter.

For example, to restart your replica set member:

> **Important:** Allow replication to catch up on this member before you begin the
next step.

### 5. Unhide the Secondary.

Run the following command on your primary to unhide the secondary node that built the index. In this example, the secondary node that built the index is the third node in `cfg.members`.

```bash
var cfg = rs.conf();
cfg.members[2].priority = originalPriority;
cfg.members[2].hidden = false;
rs.reconfig(cfg);
```

### 6. Repeat the Procedure for the Remaining Secondaries.

Once the member catches up with the other members of the set, repeat the procedure one member at a time for the remaining secondary members:

A. `Hide and restart one secondary. <tutorial-index-on-replica-sets-stop-one-member>`

B. `Build the index. <tutorial-index-on-replica-sets-build-index>`

C. `Restart the Program mongod as a replica set member. <tutorial-index-on-replica-sets-restart-mongod>`

### 7. Build the Index on the Primary.

When all the secondaries have the new index, step down the primary, restart it as a standalone using the procedure described above, and build the index on the former primary:

A. Use the :method:`rs.stepDown()` method in :binary:`~bin.mongosh` to step down the primary. Upon successful stepdown, the current primary becomes a secondary and the replica set members elect a new primary.

B. `Hide and restart one secondary. <tutorial-index-on-replica-sets-stop-one-member>`

C. `Build the index. <tutorial-index-on-replica-sets-build-index>`

D. `Restart the Program mongod as a replica set member. <tutorial-index-on-replica-sets-restart-mongod>`
