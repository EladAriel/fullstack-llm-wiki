---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-shard-key-indexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Shard Key Indexes

Sharded collections require an index that supports the `shard key`. The index can be an index on the shard key or a `compound index` where the shard key is a `prefix <compound-index-prefix>` of the index.

- If the collection is empty, :method:`sh.shardCollection()` creates
the index on the shard key if such an index does not already exists.

- If the collection is not empty, you must create the index first
before using :method:`sh.shardCollection()`.

- If you reshard a collection using
:method:`sh.reshardCollection()`, you do not need to create the index on the new shard key beforehand. The resharding operation builds the required indexes automatically. To learn more, see the `Reshard a Collection procedure <resharding_process>`.

You cannot `drop <collection-drop-index>` or `hide <collection-hide-index>` an index if it is the only non-hidden index that supports the shard key.

Starting in MongoDB 7.0.3, 6.0.12, and 5.0.22, you can drop the index for a `hashed shard key <sharding-hashed-sharding>`. For details, see `<drop-a-hashed-shard-key-index>`.

## Unique Indexes

.. include:: /includes/sharding/shard-key-indexes-unique-indexes.rst
