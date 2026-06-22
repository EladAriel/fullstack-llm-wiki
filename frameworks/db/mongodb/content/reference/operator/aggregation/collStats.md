---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/collStats.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $collStats (aggregation stage)

## Definition

## Behavior

`$collStats` must be the first stage in an aggregation pipeline, or else the pipeline returns an error.

### Accuracy After Unexpected Shutdown

.. include:: /includes/fact-unexpected-shutdown-accuracy.rst

### Redaction

When using `Queryable Encryption <qe-manual-feature-qe>`, `$collStats` output redacts certain information for encrypted collections:

- The output omits `"queryExecStats"`
- The output omits `"latencyStats"`
- The output redacts `"WiredTiger"`, if present, to include only the `url` field.
### Transactions

`$collStats` is not allowed in `transactions <transactions>`.

## Output

### latencyStats Document

The `latencyStats` embedded document only exists in the output if you specify the `latencyStats` option.

.. include:: /includes/fact-latencystats-reference.rst

High-Latency $lookup Operations ```````````````````````````````

Some high-latency :pipeline:`$lookup` operations may not generate a slow query log for the foreign collection. This can occur because slow query logs correspond with operations that are reported in the `database profiler <profiler>`, whereas latency metrics increment only when a `collection lock <faq-concurrency-locking>` is acquired.

If the `$lookup` query on a shard can perform a local read, the `$lookup` doesn't record a separate operation for querying the foreign collection. A local read refers to when the query on the foreign collection targets only the same shard where the current operation is being executed. As a result, the `$lookup` operation increases the `$collStats` latency metrics and operation counts, but does not generate a slow query log for the foreign collection.

### storageStats Document

The `storageStats` embedded document only exists in the output if you specify the `storageStats` option.

The contents of this document are dependent on the storage engine in use. See `collStats-output` for a reference on this document.

storageStats Output on Time Series Collections ``````````````````````````````````````````````

When you run `$collStats` on a time series collection with the `storageStats: {}` option, the output includes time series data.

To learn more about the fields returned in the `timeseries: {}` document, see `server-status-bucketcatalog`.

Performing `$collStats` with the `storageStats` option on a view results in an error.

### count Field

The `count` field only exists in the output if you specify the `count` option.

> **Note:** The count is based on the collection's metadata, which provides a
fast but sometimes inaccurate count for sharded clusters.

The total number of documents in the collection is also available as `storageStats.count` when `storageStats: {}` is specified. For more information, see `storage-stats-document`.

### queryExecStats Document

The `queryExecStats` embedded document only exists in the output if you specify the `queryExecStats` option. It includes an embedded `collectionScans` document with the following fields:

## Examples

> **Seealso:** - :dbcommand:`collStats`
- :method:`db.collection.stats()`
