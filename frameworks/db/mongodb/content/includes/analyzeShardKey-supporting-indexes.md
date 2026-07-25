---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-supporting-indexes.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The supporting index required by |analyzeShardKey| is different from the supporting index required by the :dbcommand:`shardCollection` command.

This table shows the supporting indexes for the same shard key for both |analyzeShardKey| and `shardCollection`:

This allows you to analyze a shard key that may not yet have a supporting index required for sharding it.

Both |analyzeShardKey| and `shardCollection` have the following index requirements:

- Index has a simple `collation <collation>`
- Index is not `multi-key <index-type-multikey>`
- Index is not `sparse <index-type-sparse>`
- Index is not `partial <index-type-partial>`
To create supporting indexes, use the :method:`db.collection.createIndex()` method.
