---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/index-creation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# Index Builds on Populated Collections

Index builds use an optimized build process that holds an exclusive lock on the collection at the beginning and end of the index build. The rest of the build process yields to interleaving read and write operations. For a detailed description of index build process and locking behavior, see `index-build-process`.

Index builds on a replica set or sharded cluster build simultaneously across all data-bearing replica set members. The primary requires a minimum number of data-bearing voting members (that is, commit quorum), including itself, that must complete the build before marking the index as ready for use. A "voting" member is any replica set member where :rsconf:`members[n].votes` is greater than `0`. See `index-operations-replicated-build` for more information.

.. include:: /includes/index-build-improvements.rst

.. include:: /includes/note-atlas-index-docs.rst

## Behavior

### Comparison to Foreground and Background Builds

Previous versions of MongoDB supported building indexes either in the foreground or background. Foreground index builds were fast and produced more efficient index data structures, but required blocking all read-write access to the parent database of the collection being indexed for the duration of the build. Background index builds were slower and produced less efficient results, but allowed read-write access to the database and its collections during the build.

Index builds now obtain an exclusive lock on the collection being indexed only at the start and end of the build. The rest of the build process uses the yielding behavior of background index builds to maximize read-write access to the collection during the build. Index builds still produce efficient index data structures despite the more permissive locking behavior.

The optimized index build performance is at least on par with background index builds. For workloads with few or no updates received during the build process, optimized index builds can be as fast as a foreground index build on that same data.

Use :method:`db.currentOp()` to monitor  the progress of ongoing index builds.

MongoDB ignores the `background` index build option if specified to :dbcommand:`createIndexes` or its shell helpers :method:`~db.collection.createIndex()` and :method:`~db.collection.createIndexes()`.

### Constraint Violations During Index Build

For indexes that enforce constraints on the collection, such as `unique <index-type-unique>` indexes, the :binary:`~bin.mongod` checks all pre-existing and concurrently-written documents for violations of those constraints after the index build completes. Documents that violate the index constraints can exist during the index build. If any documents violate the index constraints at the end of the build, the `mongod` terminates the build and throws an error.

For example, consider a populated collection `inventory`. An administrator wants to create a unique index on the `product_sku` field. If any documents in the collection have duplicate values for `product_sku`, the index build can still start successfully. If any violations still exist at the end of the build, the `mongod` terminates the build and throws an error.

Similarly, an application can successfully write documents to the `inventory` collection with duplicate values of `product_sku` while the index build is in progress.

To mitigate the risk of index build failure due to constraint violations:

- Validate that no documents in the collection violate the index
constraints.

- Stop all writes to the collection from applications that cannot
guarantee violation-free write operations.

Sharded Collections ````````````````````

For a sharded collection distributed across multiple shards, one or more shards may contain a chunk with duplicate documents. As such, the create index operation may succeed on some of the shards (that is, the ones without duplicates) but not on others (that is, the ones with duplicates). To avoid leaving inconsistent indexes across shards, you can issue the :method:`db.collection.dropIndex()` from a :binary:`~bin.mongos` to drop the index from the collection.

To mitigate the risk of this occurrence, before creating the index:

- Validate that no documents in the collection violate the index
constraints.

- Stop all writes to the collection from applications that cannot
guarantee violation-free write operations.

> **Seealso:** `index-creation-index-consistency`

### Maximum Concurrent Index Builds

By default, the server allows up to three concurrent index builds. To change the number of allowed concurrent index builds, modify the :parameter:`maxNumActiveUserIndexBuilds` parameter.

If the number of concurrent index builds reaches the limit specified by `maxNumActiveUserIndexBuilds`, the server blocks additional index builds until the number of concurrent index builds drops below the limit.

## Index Build Impact on Database Performance

### Index Builds During Write-Heavy Workloads

Building indexes when the target collection is under heavy write load can result in reduced write performance and longer index builds.

Consider designating a maintenance window during which applications stop or reduce write operations against the collection. Start the index build during this maintenance window.

### Insufficient Available System Memory (RAM)

.. include:: /includes/fact-index-build-default-memory-limit.rst

If the host machine has limited available free RAM, you may need to schedule a maintenance period to increase the total system RAM before you can modify the `mongod` RAM usage.

## Index Builds in Replicated Environments

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous-fcv.rst

.. include:: /includes/extracts/4.4-changes-index-builds-simultaneous-nolink.rst

.. include:: /includes/unreachable-node-default-quorum-index-builds.rst

The build process is summarized as follows:

1. The primary receives the :dbcommand:`createIndexes` command and
immediately creates a "startIndexBuild" oplog entry associated with the index build.

#. The secondaries start the index build after they replicate the "startIndexBuild" oplog entry.

#. Each member "votes" to commit the build once it finishes indexing data in the collection.

#. Secondary members continue to process any new write operations into the index while waiting for the primary to confirm a quorum of votes.

#. When the primary has a quorum of votes, it checks for any key constraint violations such as duplicate key errors.

- If there are no key constraint violations, the primary completes
the index build, marks the index as ready for use, and creates an associated "commitIndexBuild" oplog entry.

- If there are any key constraint violations, the index build
fails. The primary aborts the index build and creates an associated "abortIndexBuild" oplog entry.

#. The secondaries replicate the "commitIndexBuild" oplog entry and complete the index build.

If the secondaries instead replicate an "abortIndexBuild" oplog entry, they abort the index build and discard the build job.

For sharded clusters, the index build occurs only on shards containing data for the collection being indexed.

For a more detailed description of the index build process, see `index-build-process`.

By default, index builds use a commit quorum of `"votingMembers"`, or all data-bearing voting members. To start an index build with a non-default commit quorum, specify the `commitQuorum <createIndexes-cmd-commitQuorum>` parameter to :dbcommand:`createIndexes` or its shell helpers :method:`db.collection.createIndex()` and :method:`db.collection.createIndexes()`.

To modify the commit quorum required for an in-progress simultaneous index build, use the :dbcommand:`setIndexCommitQuorum` command.

.. include:: /includes/warning-simultaneous-index-builds.rst

> **Note:** Rolling index builds take at most one replica set member at a time, starting
with the secondary members, and build the index on that member as a
standalone. Rolling index builds require at least one replica set election.
Use rolling index builds only if you meet the requirements listed
on the `rolling index pages <rolling-index-build>`, as the
procedure lowers the resiliency of the cluster.

### Commit Quorum Contrasted with Write Concern

.. include:: /includes/indexes/commit-quorum-vs-write-concern.rst

## Build Failure and Recovery

### Interrupted Index Builds on Primary and Secondary `mongod`

If a primary or secondary `mongod` performs a clean :dbcommand:`shutdown` with `"force" : true` or receives a `SIGTERM` signal during an index build and the `commitQuorum <createIndexes-cmd-commitQuorum>` is set to the default `votingMembers`, the index build progress is saved to disk. The `mongod` automatically recovers the index build when restarted and continues from the saved checkpoint. In earlier versions, the index build must restart from the beginning.

The `mongod` can perform the startup process while recovering index builds.

If you restart the `mongod` as a standalone (that is, removing or commenting out :setting:`replication.replSetName` or omitting :option:`--replSetName <mongod --replSet>`), the `mongod` cannot restart the index build. The build remains in a paused state until it is manually :dbcommand:`dropped <dropIndexes>`.

### Interrupted Index Builds on Standalone `mongod`

If the `mongod` shuts down during the index build, the index build job and all progress is lost. Restarting the `mongod` does not restart the index build. You must re-issue the :method:`~db.collection.createIndex()` operation to restart the index build.

### Rollbacks during Build Process

Starting in MongoDB 5.0, if a node is rolled back to a prior state during the index build, the index build progress is saved to disk. If there is still work to be done when the rollback concludes, the `mongod` automatically recovers the index build and continues from the saved checkpoint.

MongoDB can pause an in-progress index build to perform a `rollback <replica-set-rollbacks>`.

- If the rollback does not revert the index build, MongoDB restarts
the index build after completing the rollback.

- If the rollback reverts the index build, you must re-create the
index or indexes after the rollback completes.

### Index Consistency Checks for Sharded Collections

A sharded collection has an inconsistent index if the collection does not have the exact same indexes (including the index options) on each shard that contains chunks for the collection. Although inconsistent indexes should not occur during normal operations, they can occur in the following scenarios:

- When creating an index with a `unique` key constraint and one
shard contains a chunk with duplicate documents. In such cases, the create index operation may succeed on the shards without duplicates but not on the shard with duplicates.

- When creating an index across the shards in a
`rolling manner <index-build-on-sharded-clusters>` (that is, manually building the index one by one across the shards) but either fails to build the index for an associated shard or incorrectly builds an index with different specification.

The `config server <sharding-config-server>` primary periodically checks for index inconsistencies across the shards for sharded collections. To configure these periodic checks, see :parameter:`enableShardedIndexConsistencyCheck` and :parameter:`shardedIndexConsistencyCheckIntervalMS`.

The command :dbcommand:`serverStatus` returns the field :serverstatus:`shardedIndexConsistency` to report on index inconsistencies when run on the config server primary.

To check if a sharded collection has inconsistent indexes, see `manage-indexes-find-inconsistent-indexes`.

## Monitor In Progress Index Builds

To see the status of an index build operation, you can use the :method:`db.currentOp()` method in :binary:`~bin.mongosh`. To filter the current operations for index creation operations, see `currentOp-index-creation` for an example.

The `$currentOp.msg` field includes a percentage-complete measurement of the current stage in the index build process.

### Observe Stopped and Resumed Index Builds in the Logs

While an index is being built, progress is written to the `MongoDB log<log-messages-ref>`. If an index build is stopped and resumed there will be log messages with fields like these:

```bash
 "msg":"Index build: wrote resumable state to disk",

 "msg":"Found index from unfinished build",
```

## Terminate In Progress Index Builds

Use the :dbcommand:`dropIndexes` command or its shell helpers :method:`~db.collection.dropIndex()` or :method:`~db.collection.dropIndexes()` to terminate an in-progress index build. See `dropIndexes-cmd-index-builds` for more information.

Do not use :dbcommand:`killOp` to terminate an in-progress index builds in replica sets or sharded clusters.

## Index Build Process

The following table describes each stage of the index build process:

> **Seealso:** `faq-concurrency`

## Contents

- Rolling Index Builds <core/rolling-index-builds>
