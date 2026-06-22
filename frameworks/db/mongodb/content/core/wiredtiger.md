---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/wiredtiger.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# WiredTiger Storage Engine

The WiredTiger storage engine is the default storage engine. For existing deployments, if you do not specify the `--storageEngine` or the :setting:`storage.engine` setting, the :binary:`~bin.mongod` instance can automatically determine the storage engine used to create the data files in the `--dbpath` or :setting:`storage.dbPath`.

Deployments hosted in the following environments can use the WiredTiger storage engine:

.. include:: /includes/fact-environments-atlas-only.rst

> **Note:** All {+atlas+} deployments use the WiredTiger storage engine.

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-atlas-link.rst

## Operation and Limitations

The following operational notes and limitations apply to the WiredTiger engine:

- You can't pin documents to the WiredTiger cache.
- WiredTiger doesn't reserve a portion of the cache for reads and
another for writes.

- WiredTiger allocates its cache to the entire :binary:`~bin.mongod`
instance. WiredTiger doesn't allocate cache on a per-database or per-collection level.

## Transaction (Read and Write) Concurrency

.. include:: /includes/fact-dynamic-concurrency.rst

To view the number of concurrent read transactions (read tickets) and write transactions (write tickets) allowed in the WiredTiger storage engine, use the :dbcommand:`serverStatus` command and see the :serverstatus:`queues.execution` response document.

> **Note:** A low value of :serverstatus:`available` in
:serverstatus:`queues.execution` does not indicate a cluster
overload. Use the number of queued read and write tickets as
an indication of cluster overload.

## Document Level Concurrency

WiredTiger uses document-level concurrency control for write operations. As a result, multiple clients can modify different documents of a collection at the same time.

.. include:: /includes/fact-wiredtiger-locks.rst

## Snapshots and Checkpoints

WiredTiger uses MultiVersion Concurrency Control (MVCC). At the start of an operation, WiredTiger provides a point-in-time snapshot of the data to the operation. A snapshot presents a consistent view of the in-memory data.

When writing to disk, WiredTiger writes all the data in a snapshot to disk in a consistent way across all data files. The now-`durable` data act as a checkpoint in the data files. The checkpoint ensures that the data files are consistent up to and including the last checkpoint; i.e. checkpoints can act as recovery points.

.. include:: /includes/extracts/wt-snapshot-frequency.rst

During the write of a new checkpoint, the previous checkpoint is still valid. As such, even if MongoDB terminates or encounters an error while writing a new checkpoint, upon restart, MongoDB can recover from the last valid checkpoint.

The new checkpoint becomes accessible and permanent when WiredTiger's metadata table is atomically updated to reference the new checkpoint. Once the new checkpoint is accessible, WiredTiger frees pages from the old checkpoints.

### Snapshot History Retention

Starting in MongoDB 5.0, you can use the :parameter:`minSnapshotHistoryWindowInSeconds` parameter to specify how long WiredTiger keeps the snapshot history.

Increasing the value of :parameter:`minSnapshotHistoryWindowInSeconds` increases disk usage because the server must maintain the history of older modified values within the specified time window. The amount of disk space used depends on your workload, with higher volume workloads requiring more disk space.

MongoDB maintains the snapshot history in the `WiredTigerHS.wt` file, located in your specified :setting:`~storage.dbPath`.

## Journal

WiredTiger uses a write-ahead log (i.e. journal) in combination with `checkpoints <storage-wiredtiger-checkpoints>` to ensure data durability.

The WiredTiger journal persists all data modifications between checkpoints. If MongoDB exits between checkpoints, it uses the journal to replay all data modified since the last checkpoint. For information on the frequency with which MongoDB writes the journal data to disk, see `journal-process`.

WiredTiger journal is compressed using the `snappy` compression library. To specify a different compression algorithm or no compression, use the :setting:`storage.wiredTiger.engineConfig.journalCompressor` setting. For details on changing the journal compressor, see `manage-journaling-change-wt-journal-compressor`.

> **Note:** .. include:: /includes/extracts/wt-log-compression-limit.rst

> **Seealso:** `Journaling with WiredTiger <journaling-wiredTiger>`

## Compression

With WiredTiger, MongoDB supports compression for all collections and indexes. Compression minimizes storage use at the expense of additional CPU.

By default, WiredTiger uses block compression with the `snappy` compression library for most collections and `prefix compression` for all indexes. However, the default block compression for time-series collections is `zstd`.

For collections, the following block compression libraries are also available:

- `zlib`
- `zstd`
To specify an alternate compression algorithm or no compression, use the :setting:`storage.wiredTiger.collectionConfig.blockCompressor` setting.

For indexes, to disable `prefix compression`, use the :setting:`storage.wiredTiger.indexConfig.prefixCompression` setting.

Compression settings are also configurable on a per-collection and per-index basis during collection and index creation. See `create-collection-storage-engine-options` and `db.collection.createIndex() storageEngine option <createIndex-options>`.

For most workloads, the default compression settings balance storage efficiency and processing requirements.

The WiredTiger journal is also compressed by default. For information on journal compression, see `storage-wiredtiger-journal`.

## Memory Use

.. include:: /includes/extracts/wt-cache-utilization.rst

.. include:: /includes/extracts/wt-cache-setting.rst

.. include:: /includes/extracts/wt-filesystem-cache.rst

.. include:: /includes/extracts/wt-cache-additional-constraints-mongod-cmdline-option.rst
