---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/release-notes/fsync-fsyncUnlock.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 7.1, the :dbcommand:`fsync` and :dbcommand:`fsyncUnlock` commands can perform fsync operations on sharded clusters.

When run on :program:`mongos` with the `lock` field set to `true`, the :dbcommand:`fsync` command flushes writes from the storage layer to disk and locks each shard, preventing additional writes. The :dbcommand:`fsyncUnlock` command can then be used to unlock the cluster.

This feature enables self-managed backups of sharded clusters using :program:`mongodump`.
