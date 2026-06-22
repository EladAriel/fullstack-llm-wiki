---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/faq/storage.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# FAQ: MongoDB Storage for Self-Managed Deployments

This document addresses common questions regarding MongoDB's storage system.

## Storage Engine Fundamentals

### What is a storage engine?

A storage engine is the part of a database that is responsible for managing how data is stored, both in memory and on disk. Many databases support multiple storage engines, where different engines perform better for specific workloads. For example, one storage engine might offer better performance for read-heavy workloads, and another might support a higher throughput for write operations.

> **Seealso:** `/core/storage-engines`

## Can you mix storage engines in a replica set?

Yes. You can have replica set members that use different storage engines (WiredTiger and in-memory)

## Storage Recommendations

### How many collections and indexes can be in a cluster?

Cluster performance might degrade once the combined number of collections and indexes reaches beyond 100,000. In addition, many large collections have a greater impact on performance than smaller collections.

## WiredTiger Storage Engine

### Can I upgrade an existing deployment to WiredTiger?

Yes. See:

- `/tutorial/change-standalone-wiredtiger`
- `/tutorial/change-replica-set-wiredtiger`
- `/tutorial/change-sharded-cluster-wiredtiger`
### How much compression does WiredTiger provide?

The ratio of compressed data to uncompressed data depends on your data and the compression library used. By default, collection data in WiredTiger use `Snappy block compression <snappy>`; `zlib` and `zstd` compression is also available. Index data use `prefix compression` by default.

### To what size should I set the WiredTiger internal cache?

.. include:: /includes/extracts/wt-configure-cache.rst

### How much memory does MongoDB allocate per connection?

Each connection uses up to 1 megabyte of RAM.

To optimize memory use for connections, ensure that you:

- Monitor the number of open connections to your deployment. Too many
open connections result in excessive use of RAM and reduce available memory for the `working set`.

- Close `connection pools <connection-pool-overview>` when they are
no longer needed. A connection pool is a cache of open, ready-to-use database connections maintained by the driver. Closing unneeded pools makes additional memory resources available.

- Manage the size of your connection pool. The :urioption:`maxPoolSize`
connection string option specifies the maximum number of open connections in the pool. By default, you can have up to 100 open connections in the pool. Lowering the `maxPoolSize` reduces the maximum amount of RAM used for connections.

> **Tip:**   To configure your connection pool, see
  `connection-pool-settings`.

### How frequently does WiredTiger write to disk?

Checkpoints

.. include:: /includes/extracts/wt-snapshot-frequency.rst

Journal Data

.. include:: /includes/extracts/wt-journal-frequency.rst

### How do I reclaim disk space in WiredTiger?

The WiredTiger storage engine maintains lists of empty records in data files as it deletes documents. This space can be reused by WiredTiger, but will not be returned to the operating system unless under very specific circumstances.

The amount of empty space available for reuse by WiredTiger is reflected in the output of :method:`db.collection.stats()` under the heading `wiredTiger.block-manager.file bytes available for reuse`.

To allow the WiredTiger storage engine to release this empty space to the operating system, you can de-fragment your data file. This can be achieved by `resyncing a replica set member <resync-replica-member>` or using the :dbcommand:`compact` command.

## Data Storage Diagnostics

### How can I check the size of a collection?

To view the statistics for a collection, including the data size, use the :method:`db.collection.stats()` method from within :binary:`~bin.mongosh`. The following example issues :method:`db.collection.stats()` for the `orders` collection:

```javascript
db.orders.stats();
```

MongoDB also provides the following methods to return specific sizes for the collection:

- :method:`db.collection.dataSize()` to return the uncompressed data
size in bytes for the collection.

- :method:`db.collection.storageSize()` to return the size in bytes of
the collection on disk storage. If collection data is compressed (which is the :option:`default for WiredTiger <mongod --wiredTigerCollectionBlockCompressor>`), the storage size reflects the compressed size and may be smaller than the value returned by :method:`db.collection.dataSize()`.

- :method:`db.collection.totalIndexSize()` to return the index sizes in
bytes for the collection. If an index uses prefix compression (which is the :option:`default for WiredTiger <mongod --wiredTigerIndexPrefixCompression>`), the returned size reflects the compressed size.

The following script prints the statistics for each database:

```javascript
db.adminCommand("listDatabases").databases.forEach(function (d) {
   mdb = db.getSiblingDB(d.name);
   printjson(mdb.stats());
})
```

The following script prints the statistics for each collection in each database:

```javascript
db.adminCommand("listDatabases").databases.forEach(function (d) {
   mdb = db.getSiblingDB(d.name);
   mdb.getCollectionNames().forEach(function(c) { 
      s = mdb[c].stats();
      printjson(s);
   })
})
```

### How can I check the size of the individual indexes for a collection?

To view the size of the data allocated for each index, use the :method:`db.collection.stats()` method and check the `collStats.indexSizes` field in the returned document.

If an index uses prefix compression (which is the :option:`default for WiredTiger <mongod --wiredTigerIndexPrefixCompression>`), the returned size for that index reflects the compressed size.

### How can I get information on the storage use of a database?

The :method:`db.stats()` method in :binary:`~bin.mongosh` returns the current state of the "active" database. For the description of the returned fields, see `dbStats Output <dbstats-output>`.
