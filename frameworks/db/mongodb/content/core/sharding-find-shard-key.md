---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharding-find-shard-key.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
