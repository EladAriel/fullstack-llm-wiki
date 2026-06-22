---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-sync.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# Replica Set Data Synchronization

To maintain up-to-date copies of the shared data set, secondary members of a replica set `sync` or replicate data from a |source|. MongoDB uses two forms of data synchronization: initial sync to populate new members with the full data set, and replication to apply ongoing changes to the entire data set.

## Initial Sync

Initial sync copies all the data from the |source| of the replica set to a |destin|. See `replica-set-initial-sync-source-selection` for more information on |source| selection criteria.

The `local` database stores the `oplog` data that the initial sync process uses. Ensure the |destin| has enough space in the `local` database to store the oplog data for the initial sync process to complete.

> **Note:** During the initial sync, MongoDB truncates the oplog on the |destin|. This
oplog truncation can impact processes, such as :ref:`change streams
<changeStreams>`, that depend on oplog data.

You can specify the preferred initial sync source using the :parameter:`initialSyncSourceReadPreference` parameter. This parameter can only be specified when starting the :binary:`~bin.mongod`.

Starting in MongoDB 5.2, initial syncs can be logical or file copy based.

> **Note:** For self-managed deployments, initial sync is the process that
MongoDB uses to add a new node to a replica set. This is different
from `cloud-based initial syncs <cloud-based-initial-sync>`
available in {+atlas+}, which leverage your cloud provider's native
capabilities to create a snapshot of the source node's data and
restore it to the new node.

### Logical Initial Sync Process

When you perform a logical initial sync, MongoDB:

#. Clones all databases except the `local <replica-set-local-database>` database. To clone, the :binary:`~bin.mongod` scans every collection in each |source| database and inserts all data into its own copies of these collections.

#. In parallel with the data clone, `mongod` builds all collection indexes as it copies all the documents for each collection.

#. Applies oplog records that buffered during the data copy.

#. Applies all changes to the data set. Using the oplog from the |source|, the :binary:`~bin.mongod` updates its data set to reflect the current state of the replica set.

> **Important:** * During steps 1 and 2, the `mongod` pulls newly added oplog records and
  stores them in a temporary collection in the `local` database. Ensure that
  the target member has enough disk space in the `local` database to temporarily
  store these oplog records for the duration of this data copy stage.
* During steps 3 and 4, the syncing node checks for continuity of operations
  against the source node. If a gap is found, restart the initial sync from
  the beginning. To avoid this, make sure that the size of the oplog provisioned
  provides enough of an oplog window to cover the time it takes for steps 3
  and 4 to complete.

When the initial sync finishes, the member transitions from :replstate:`STARTUP2` to :replstate:`SECONDARY`.

To perform an initial sync, see `resync-replica-member`.

### File Copy Based Initial Sync

Available in MongoDB Enterprise only.

File copy based initial sync runs the initial sync process by copying and moving files on the file system. This sync method can be faster than `logical initial sync <replica-set-initial-sync-logical>`.

> **Important:** After file copy based initial sync completes, if you run the
:method:`~db.collection.count()` method without a query predicate, the
count of documents returned may be inaccurate.
A `count` method without a query predicate looks like this:
`db.<collection>.count()`.
To learn more, see `count-method-behavior-query-predicate`.

Enable File Copy Based Initial Sync ```````````````````````````````````

To enable file copy based initial sync, set the :parameter:`initialSyncMethod` parameter to `fileCopyBased` on the |destin| for the initial sync. This parameter can only be set at startup.

Behavior ````````

File copy based initial sync replaces the `local` database of the |destin| with the `local` database of the source member when syncing.

Limitations ```````````

- During a file copy based initial sync:
- You cannot run backups on either the |source| or the |destin|.
- You cannot write to the `local` database on the |destin|.
- You can only run an initial sync from one |source| at a time.
- When using the encrypted storage engine, MongoDB uses the |source|
key to encrypt the destination.

### Initial Sync on NVMe Clusters

You must perform an initial sync on clusters that use the local Non-Volatile Memory Express (`NVMe`) SSD storage option, including if you're using Atlas `auto-scaling <cluster-autoscaling>`. Atlas NVMe clusters auto-scale to the next higher tier when 90% of the storage space is full. An initial sync takes longer to complete compared to subsequent syncs, and reduces the performance of the `primary` from which the data is read.

### Fault Tolerance

If a |destin| performing initial sync encounters a persistent network error during the sync process, the |destin| restarts the initial sync process from the beginning.

A |destin| performing initial sync can attempt to resume the sync process if interrupted by a temporary network error, collection drop, or collection rename.

By default, the |destin| tries to resume initial sync for 24 hours. You can use the :parameter:`initialSyncTransientErrorRetryPeriodSeconds` server parameter to control the amount of time the |destin| attempts to resume initial sync. If the |destin| cannot successfully resume the initial sync process during the configured time period, it selects a new healthy |source| from the replica set and restarts the initial synchronization process from the beginning.

The secondary attempts to restart the initial sync up to `10` times before returning a fatal error.

### Initial Sync Source Selection

Initial sync source selection depends on the value of the :binary:`~bin.mongod` startup parameter :parameter:`initialSyncSourceReadPreference`:

- For :parameter:`initialSyncSourceReadPreference` set to
:readmode:`primary` (default if :rsconf:`chainingAllowed <settings.chainingAllowed>` is disabled), select the `primary` as the |source|. If the primary is unavailable or unreachable, log an error and periodically check for primary availability.

- For :parameter:`initialSyncSourceReadPreference` set to
:readmode:`primaryPreferred` (default for voting replica set members), attempt to select the `primary` as the |source|. If the primary is unavailable or unreachable, perform sync |source| selection from the remaining replica set members.

- For all other supported read modes, perform sync |source| selection
from the |destins|.

Members performing initial |source| selection make two passes through the list of all replica set members:

If the |destin| cannot select a |source| after two passes, it logs an error and waits `1` second before restarting the selection process. The secondary :binary:`~bin.mongod` can restart the initial sync source selection process up to `10` times before exiting with an error.

### Oplog Window

The `oplog window` must be long enough so that a |destin| can fetch any new `oplog` entries that occur between the start and end of the `replica-set-initial-sync-logical`. If the window is too short, some entries may fall off the `oplog` before the |destin| can apply them.

Size the `oplog` with additional time to accommodate changes that may occur during initial syncs.

For more information, see `replica-set-oplog-sizing`.

## Replication

|Destins| replicate data continuously after the initial sync. |Destins| copy the `oplog <replica-set-oplog>` from the |source| and apply these operations in an asynchronous process.

|Destins| automatically change their |source| as needed based on changes in the ping time and state of other members' replication. See `replica-set-replication-sync-source-selection` for more information on |source| selection criteria.

### Streaming Replication

|Sources| send a continuous stream of `oplog <replica-set-oplog>` entries to their |destins|. Streaming replication mitigates replication lag in high-load and high-latency networks. It also:

- Reduces staleness for reads from secondaries.
- Reduces risk of losing write operations with `w: 1 <wc-w>` due to
primary failover.

- Reduces latency on write operations with :writeconcern:`w: "majority"
<"majority">` and `w: >1 <wc-w>` (that is, any write concern that requires waiting for replication).

Use the :parameter:`oplogFetcherUsesExhaust` startup parameter to disable streaming replication and using the older replication behavior. Set the :parameter:`oplogFetcherUsesExhaust` parameter to `false` only if there are any resource constraints on the |source| or if you wish to limit MongoDB's usage of network bandwidth for replication.

### Multithreaded Replication

MongoDB applies write operations in batches using multiple threads to improve concurrency. MongoDB groups batches by document ID (`WiredTiger <storage-wiredtiger>`) and simultaneously applies each group of operations using a different thread. MongoDB always applies write operations to a given document in their original write order.

Read operations that `target secondaries <replica-set-read-preference>` and are configured with a `read concern<read-concern>` level of :readconcern:`"local"` or  :readconcern:`"majority"` read from a `WiredTiger<storage-wiredtiger>` snapshot of the data if the read takes place on a secondary where replication batches are being applied.

Reading from a snapshot guarantees a consistent view of the data, and allows the read to occur simultaneously with the ongoing replication without the need for a lock. As a result, secondary reads requiring these read concern levels no longer need to wait for replication batches to be applied, and can be handled as they are received.

### Flow Control

.. include:: /includes/extracts/4.2-changes-flow-control-general-desc.rst

For more information, see `flow-control`.

### Replication Sync Source Selection

Replication |source| selection depends on the replica set :rsconf:`chaining <settings.chainingAllowed>` setting:

- With chaining enabled (default), perform |source| selection from
the |destins|.

- With chaining disabled, select the `primary` as the |source|.
If the primary is unavailable or unreachable, log an error and periodically check for primary availability.

Members performing replication |source| selection make two passes through the list of all replica set members:

If the member cannot select a sync source after two passes, it logs an error and waits `1` second before restarting the selection process.

The number of times a |source| can be changed per hour is configurable by setting the :parameter:`maxNumSyncSourceChangesPerHour` parameter.

> **Note:** The startup parameter :parameter:`initialSyncSourceReadPreference` takes
precedence over the replica set's :rsconf:`settings.chainingAllowed` setting
when selecting an initial sync |source|. After a replica set member
successfully performs initial sync, it defers to the value of
:rsconf:`~settings.chainingAllowed` when selecting a |source|.
See `replica-set-initial-sync-source-selection` for more
information on initial sync source selection.
