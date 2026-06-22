---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/drop-a-hashed-shard-key-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Drop a Hashed Shard Key Index

.. include:: /includes/drop-hashed-shard-key-index-main.rst

## About this Task

Dropping an `unnecessary index <unnecessary-indexes-antipattern>` can speed up CRUD operations. Each CRUD operation has to update all the indexes related to a document. Removing one index can increase the speed of all CRUD operations.

> **Important:** You should only drop a hashed shard key index from a collection
if a supporting non-hashed index on the shard key exists. If a
supporting non-hashed index does not exist on the shard key, queries
filtering by the shard key perform a `collection scan`.
To see what indexes exist on a collection, use
:method:`db.collection.getIndexes()`.

## Considerations

When dropping a hashed shard key index, consider the following:

- The server disables balancing for your collection and excludes
the collection from future balancing rounds. As a result, if you later add or remove a shard, the server cannot rebalance the collection's data. To include the collection in future balancing rounds, recreate the hashed shard key index.

- When you drop the shard key index, the range deleter does not clean up
any remaining orphans in your collection. You must confirm that no orphaned documents exist in your collection before dropping the hashed shard key index. See the below procedure for how to confirm that there are no orphaned documents in your collection.

## Steps

## Learn More

- `sharding-hashed`
- `sharding-balancing`
- :method:`db.collection.dropIndex()`
- :method:`sh.stopBalancer()`
- :method:`sh.startBalancer()`
- :method:`sh.getBalancerState()`
