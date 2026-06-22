---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/command/unshardCollection.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Unshards an existing sharded collection and moves the collection data onto a single shard. When you unshard a collection, the collection cannot be partitioned across multiple `shards <shard>` and the `shard key` is removed.

.. versionadded:: 8.0
