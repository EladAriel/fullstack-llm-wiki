---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/release-notes/fsync-fsyncUnlock.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 7.1, the :dbcommand:`fsync` and :dbcommand:`fsyncUnlock` commands can perform fsync operations on sharded clusters.

When run on :program:`mongos` with the `lock` field set to `true`, the :dbcommand:`fsync` command flushes writes from the storage layer to disk and locks each shard, preventing additional writes. The :dbcommand:`fsyncUnlock` command can then be used to unlock the cluster.

This feature enables self-managed backups of sharded clusters using :program:`mongodump`.
