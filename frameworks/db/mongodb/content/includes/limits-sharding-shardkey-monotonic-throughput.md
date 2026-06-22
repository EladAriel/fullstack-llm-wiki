---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/limits-sharding-shardkey-monotonic-throughput.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For clusters with high insert volumes, a shard key with monotonically increasing and decreasing keys can affect insert throughput. If your shard key is the `_id field, be aware that the default values of the id` fields are `ObjectIds <ObjectId>` which have generally increasing values.

When inserting documents with monotonically increasing shard keys, all inserts belong to the same `chunk` on a single `shard`. The system eventually divides the chunk range that receives all write operations and migrates its contents to distribute data more evenly. However, at any moment the cluster directs insert operations only to a single shard, which creates an insert throughput bottleneck.

If the operations on the cluster are predominately read operations and updates, this limitation may not affect the cluster.

To avoid this constraint, use a `hashed shard key <sharding-hashed-sharding>` or select a field that does not increase or decrease monotonically.

`Hashed shard keys <sharding-hashed-sharding>` and `hashed indexes <index-type-hashed>` store hashes of keys with ascending values.
