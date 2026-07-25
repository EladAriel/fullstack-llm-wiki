---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-find-shard-key.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================

# Display a Shard Key

Every sharded collection has a `shard key <sharding-shard-key>`. To display the shard key, connect to a :binary:`mongos` instance and run the :method:`db.printShardingStatus()` method:

```javascript
db.printShardingStatus()
```

The output resembles:

.. include:: /includes/reference/sharded-status-output.rst

For more details on the `db.printShardingStatus()` output, see the `sharded collection section <sharded-collection-output-reference>` on the :method:`sh.status()` page.
