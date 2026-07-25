---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/command/unshardCollection.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Unshards an existing sharded collection and moves the collection data onto a single shard. When you unshard a collection, the collection cannot be partitioned across multiple `shards <shard>` and the `shard key` is removed.

.. versionadded:: 8.0
