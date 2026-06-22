---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/shard-a-collection.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You can use the :binary:`~bin.mongosh` method :method:`sh.shardCollection()` to shard a collection. To shard a collection, you must specify the full namespace of the collection that you want to shard and the shard key.

```javascript
sh.shardCollection(<namespace>, <key>) // Optional parameters omitted
```

For more information on the sharding method, see :method:`sh.shardCollection()`.
