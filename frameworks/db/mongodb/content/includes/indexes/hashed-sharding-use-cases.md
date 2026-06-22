---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/hashed-sharding-use-cases.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Hashed indexing is ideal for shard keys with fields that change `monotonically <shard-key-monotonic>` like `ObjectId` values or timestamps. When you use `ranged sharding <sharding-ranged>` with a monotonically increasing shard key value, the chunk with an upper bound of :bsontype:`MaxKey` receives the majority incoming writes. This behavior restricts insert operations to a single shard, which removes the advantage of distributed writes in a sharded cluster.

For more information on choosing the best sharding approach for your application, see `hashed-versus-ranged-sharding`
