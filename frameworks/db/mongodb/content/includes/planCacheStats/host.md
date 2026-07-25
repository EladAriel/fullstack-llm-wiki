---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/planCacheStats/host.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The hostname and port of the :binary:`~bin.mongod` instance from which the plan cache information was returned.

When run on a sharded cluster, the operation returns plan cache entry information from a single member in each shard replica set. This member is identified with the `shard <plancachestats-shard>` and `host <plancachestats-host>` fields. See also `plancachestats-read-pref`.
