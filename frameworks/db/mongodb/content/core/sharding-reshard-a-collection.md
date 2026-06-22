---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-reshard-a-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Reshard a Collection

The ideal shard key allows MongoDB to distribute documents evenly throughout the cluster while facilitating common query patterns. A suboptimal shard key can lead to performance or scaling issues due to uneven data distribution. You can change the shard key for a collection to change the distribution of your data across a cluster.

Starting in MongoDB 8.0, you can reshard a collection on the same shard key, allowing you to redistribute data to include new shards or to different zones without changing your shard key. To reshard to the same shard key, set `forceRedistribution <forceRedistribution-field>` to `true`.

.. include:: /includes/time-series/reshard-timeseries.rst

> **Note:** Before resharding your collection, read
`shardkey-troubleshoot-shard-keys` for information on common
performance and scaling issues and advice on how to fix them.

## About this Task

.. include:: /includes/sharding/resharding-limitations.rst

## Before you Begin

.. include:: /includes/fact-reshard-considerations.rst

- You must rewrite your application's queries to use **both** the
current shard key and the new shard key.

> **Tip:**   If your application can tolerate downtime, you can perform these
  steps to avoid rewriting your application's queries to use both the
  current and new shard keys:
  #. Stop your application.
  #. Rewrite your application to use the **new** shard key.
  #. Wait until the resharding operation completes. To
     monitor the resharding process, use the
     :pipeline:`$currentOp` pipeline stage.
  #. Deploy your rewritten application.
Before the resharding operation completes, the following
queries return an error if the query filter does not include
either the current shard key or a unique field (like `_id`):
- :method:`~db.collection.deleteOne()`
- :method:`~db.collection.findAndModify()`
- :method:`~db.collection.findOneAndDelete()`
- :method:`~db.collection.findOneAndReplace()`
- :method:`~db.collection.findOneAndUpdate()`
- :method:`~db.collection.replaceOne()`
- :method:`~db.collection.updateOne()`
For optimal performance, we recommend that you also rewrite other
queries to include the new shard key.
Once the resharding operation completes, you can remove the
old shard key from the queries.

.. include:: /includes/resharding-oplog-note.rst

## Steps

> **Important:** We strongly recommend that you check the
`resharding-limitations` and read the `resharding_process`
section in full before resharding your collection.

.. include:: /includes/reshard-collection-introduction.rst

.. include:: /includes/steps/reshard-a-collection.rst

## Behavior

### Minimum Duration of a Resharding Operation

The minimum duration of a resharding operation is always 5 minutes.

### Retryable Writes

`Retryable writes <retryable-writes>` initiated before or during resharding can be retried during and after the collection has been resharded for up to 5 minutes. After 5 minutes you may be unable to find the definitive result of the write and subsequent attempts to retry the write fail with an `IncompleteTransactionHistory` error.

### Reshard Limitations

.. include:: /includes/fact-reshard-limitations.rst

## Error Case

### Duplicate `_id` Values

The resharding operation fails if `_id values are not globally unique to avoid corrupting collection data. Duplicate id values can also prevent successful chunk migration. If you have documents with duplicate id` values, copy the data from each into a new document, and then delete the duplicate documents.
