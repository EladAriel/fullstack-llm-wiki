---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/shard-a-collection.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can use the :binary:`~bin.mongosh` method :method:`sh.shardCollection()` to shard a collection. To shard a collection, you must specify the full namespace of the collection that you want to shard and the shard key.

```javascript
sh.shardCollection(<namespace>, <key>) // Optional parameters omitted
```

For more information on the sharding method, see :method:`sh.shardCollection()`.
