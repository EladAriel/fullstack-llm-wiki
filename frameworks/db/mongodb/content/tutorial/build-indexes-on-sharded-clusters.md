---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/build-indexes-on-sharded-clusters.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================================

# Create Rolling Index Builds on Sharded Clusters

## About this Task

Rolling index builds are an alternative to `default index builds <index-operations>`.

.. include:: /includes/warning-simultaneous-index-builds.rst

## Considerations

> **Warning:** Make sure you are not performing `DDL operations <ddl-operations>` while conducting the rolling index build.

### Unique Indexes

To create `unique indexes <index-type-unique>` using the following procedure, you must stop all writes to the collection during this procedure.

If you cannot stop all writes to the collection during this procedure, do not use the procedure on this page. Instead, build your unique index on the collection by issuing :method:`db.collection.createIndex()` on the :binary:`~bin.mongos` for a sharded cluster.

### Oplog Size

Ensure that your `oplog` is large enough to permit the indexing or re-indexing operation to complete without falling too far behind to catch up. See the `oplog sizing <replica-set-oplog-sizing>` documentation for additional information.

Rolling index builds lower the resiliency of your cluster and increase build duration.

## Before You Begin

For building unique indexes #. To create `unique indexes <index-type-unique>` using the following procedure, you must stop all writes to the collection during the index build. Otherwise, you may end up with inconsistent data across the replica set members. If you cannot stop all writes to the collection, do not use the following procedure to create unique indexes.

> **Warning:**       If you cannot stop all writes to the collection, do not use the
      following procedure to create unique indexes.
#. Before creating the index, validate that no documents in the
   collection violate the index constraints. If a collection is
   distributed across shards and a shard contains a chunk with
   duplicate documents, the create index operation may succeed on the
   shards without duplicates but not on the shard with duplicates.
   To avoid leaving inconsistent indexes across shards, you can issue the
   :method:`db.collection.dropIndex()` from a :binary:`~bin.mongos` to
   drop the index from the collection.

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Procedure

> **Important:** The following procedure to build indexes in a rolling fashion applies
to sharded clusters deployments, and not replica set deployments. For
the procedure for replica sets, see
`/tutorial/build-indexes-on-replica-sets` instead.

### A. Stop Migrations

Connect :binary:`~bin.mongosh` to a :binary:`~bin.mongos` instance in the sharded cluster and disable migrations for the collection where you want to perform the rolling build index:

```javascript
db.adminCommand(
 {
   setAllowMigrations: "<db>.<collection>",
   allowMigrations: false
 }
)
```

The preceding command ensures the correct set of shards is targeted for rolling index builds because no migration for the collection will be allowed to commit.

If the command returns the following error, it means the collection is unsharded. You can safely ignore the error and continue with the next step.

```javascript
MongoServerError[NamespaceNotSharded]: Collection must be sharded so migrations can be blocked
```

### B. Determine the Distribution of the Collection

To determine which shards must be involved in the rolling index build, run the following aggregation on the collection that you want to build the index on:

```javascript
db.getSiblingDB(<db>).getCollection(<collection>).aggregate([{$collStats:{}},{$group: {_id: "$ns", shard_list: {$addToSet: "$shard"}}}])
```

For example, if you want to create an index on the `records` collection in the `test` database:

From the output, you only build the indexes for `test.records` on `shardA` and `shardC`.

### C. Build Indexes on the Shards That Contain Collection Chunks

For each shard that contains chunks for the collection, follow the procedure to build the index on the shard.

C1. Stop One Secondary and Restart as a Standalone ``````````````````````````````````````````````````

For an affected shard, stop the :binary:`~bin.mongod` process associated with one of its secondary. Restart after making the following configuration updates:

port, you ensure that the other members of the replica set and all clients will not contact the member while you are building the index.

C2. Build the Index ```````````````````

Connect directly to the :binary:`~bin.mongod` instance running as a standalone on the new port and create the new index for this instance.

For example, connect :binary:`~bin.mongosh` to the instance, and use the :method:`db.collection.createIndex()` method to create an ascending index on the `username` field of the `records` collection:

```bash
db.records.createIndex( { username: 1 } )
```

C3. Restart the Program `mongod` as a Replica Set Member ``````````````````````````````````````````````````````````

When the index build completes, shutdown the :binary:`~bin.mongod` instance. Undo the configuration changes made when starting as a standalone to return to its original configuration and restart.

> **Important:** Be sure to remove the
:parameter:`skipShardingConfigurationChecks` parameter and
`disableLogicalSessionCacheRefresh` parameter.

For example, to restart your replica set shard member:

Allow replication to catch up on this member.

C4. Repeat the Procedure for the Remaining Secondaries for the Shard ````````````````````````````````````````````````````````````````````

Once the member catches up with the other members of the set, repeat the procedure one member at a time for the remaining secondary members for the shard:

#. `tutorial-index-on-sharded-clusters-stop-one-member`

#. `tutorial-index-on-sharded-clusters-build-index`

#. `tutorial-index-on-sharded-clusters-restart-mongod`

C5. Build the Index on the Primary ``````````````````````````````````

When all the secondaries for the shard have the new index, step down the primary for the shard, restart it as a standalone using the procedure described above, and build the index on the former primary:

#. Use the :method:`rs.stepDown()` method in :binary:`~bin.mongosh` to step down the primary. Upon successful stepdown, the current primary becomes a secondary and the replica set members elect a new primary.

#. `tutorial-index-on-sharded-clusters-stop-one-member`

#. `tutorial-index-on-sharded-clusters-build-index`

#. `tutorial-index-on-sharded-clusters-restart-mongod`

### D. Repeat for the Other Affected Shards

Once you finish building the index for a shard, repeat `tutorial-index-on-affected-shards` for the other affected shards.

### E. Enable Migrations

Connect :binary:`~bin.mongosh` to a :binary:`~bin.mongos` instance in the sharded cluster and re-enable the migration with :dbcommand:`setAllowMigrations`:

```javascript
db.adminCommand(
 {
   setAllowMigrations: "<db>.<collection>",
   allowMigrations: true
 }
)
```

If the command returns the following error, it means the collection is unsharded. You can safely ignore the error.

```javascript
MongoServerError[NamespaceNotSharded]: Collection must be sharded so migrations can be blocked
```

## Additional Information

A sharded collection has an inconsistent index if the collection does not have the exact same indexes (including the index options) on each shard that contains chunks for the collection. Although inconsistent indexes should not occur during normal operations, inconsistent indexes can occur, such as:

- When a user is creating an index with a `unique` key constraint and
one shard contains a chunk with duplicate documents. In such cases, the create index operation may succeed on the shards without duplicates but not on the shard with duplicates.

- When a user is creating an index across the shards in a rolling
manner but either fails to build the index for an associated shard or incorrectly builds an index with different specification.

The `config server <sharding-config-server>` primary periodically checks for index inconsistencies across the shards for sharded collections. To configure these periodic checks, see :parameter:`enableShardedIndexConsistencyCheck` and :parameter:`shardedIndexConsistencyCheckIntervalMS`.

The command :dbcommand:`serverStatus` returns the field :serverstatus:`shardedIndexConsistency` to report on index inconsistencies when run on the config server primary.

To check if a sharded collection has inconsistent indexes, see `manage-indexes-find-inconsistent-indexes`.
