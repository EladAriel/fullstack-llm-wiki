---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/journaling.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========

# Journaling

To provide durability in the event of a failure, MongoDB uses write ahead logging to on-disk `journal` files.

## Journaling and the WiredTiger Storage Engine

> **Important:** The log mentioned in this section refers to the WiredTiger
write-ahead log (i.e. the journal) and not the MongoDB log file.

`WiredTiger <storage-wiredtiger>` uses `checkpoints <storage-wiredtiger-checkpoints>` to provide a consistent view of data on disk and allow MongoDB to recover from the last checkpoint. However, if MongoDB exits unexpectedly in between checkpoints, journaling is required to recover information that occurred after the last checkpoint.

> **Note:** .. include:: /includes/journal-option-removed.rst

With journaling, the recovery process:

#. Looks in the data files to find the identifier of the last checkpoint.

#. Searches in the journal files for the record that matches the identifier of the last checkpoint.

#. Apply the operations in the journal files since the last checkpoint.

### Journaling Process

With journaling, WiredTiger creates one journal record for each client initiated write operation. The journal record includes any internal write operations caused by the initial write. For example, an update to a document in a collection may result in modifications to the indexes; WiredTiger creates a single journal record that includes both the update operation and its associated index modifications.

MongoDB configures WiredTiger to use in-memory buffering for storing the journal records. Threads coordinate to allocate and copy into their portion of the buffer. All journal records up to 128 kB are buffered.

.. include:: /includes/extracts/wt-journal-frequency.rst

> **Important:** In between write operations, while the journal records
remain in the WiredTiger buffers, updates can be lost following a
hard shutdown of :binary:`~bin.mongod`.

> **Seealso:** The :dbcommand:`serverStatus` command returns information on the
WiredTiger journal statistics in the :serverstatus:`wiredTiger.log`
field.

### Journal Files

For the journal files, MongoDB creates a subdirectory named `journal` under the :setting:`~storage.dbPath` directory. WiredTiger journal files have names with the following format `WiredTigerLog.<sequence>` where `<sequence>` is a zero-padded number starting from `0000000001`.

Journal Records ```````````````

Journal files contain a record per each client initiated write operation

- The journal record includes any internal write operations caused by
the initial write. For example, an update to a document in a collection may result in modifications to the indexes; WiredTiger creates a single journal record that includes both the update operation and its associated index modifications.

- Each record has a unique identifier.
- The minimum journal record size for WiredTiger is 128 bytes.
Compression ```````````

By default, MongoDB configures WiredTiger to use snappy compression for its journaling data. To specify a different compression algorithm or no compression, use the :setting:`storage.wiredTiger.engineConfig.journalCompressor` setting. For details, see `manage-journaling-change-wt-journal-compressor`.

> **Note:** .. include:: /includes/extracts/wt-log-compression-limit.rst

Journal File Size Limit ```````````````````````

WiredTiger journal files have a maximum size limit of approximately 100 MB. Once the file exceeds that limit, WiredTiger creates a new journal file.

WiredTiger automatically removes old journal files and maintains only the files needed to recover from the last checkpoint.  To determine how much disk space to set aside for journal files, consider the following:

- The default maximum size for a checkpoint is 2 GB
- Additional space may be required for MongoDB to write new journal
files while recovering from a checkpoint

- MongoDB compresses journal files
- The time it takes to restore a checkpoint is specific to your use case
- If you override the maximum checkpoint size or disable compression, your
calculations may be significantly different

For these reasons, it is difficult to calculate exactly how much additional space you need. Over-estimating disk space is always a safer approach.

> **Important:** If you do not set aside enough disk space for your journal
files, the MongoDB server will crash.

Pre-Allocation ``````````````

WiredTiger pre-allocates journal files.

## Journaling and the In-Memory Storage Engine

In MongoDB Enterprise, the `In-Memory Storage Engine </core/inmemory>` is part of general availability (GA). Because its data is kept in memory, there is no separate journal. Write operations with a write concern of :writeconcern:`j: true <j>` are immediately acknowledged.

.. include:: /includes/extracts/no-journaling-writeConcernMajorityJournalDefault-false.rst

> **Note:** .. include:: /includes/extracts/4.2-changes-inmem-startup-warning.rst

.. include:: /includes/extracts/no-journaling-rollback.rst

> **Seealso:** `In-Memory Storage Engine: Durability <inmemory-durability>`
