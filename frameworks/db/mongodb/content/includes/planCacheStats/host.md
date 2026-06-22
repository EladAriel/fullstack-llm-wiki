---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/planCacheStats/host.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The hostname and port of the :binary:`~bin.mongod` instance from which the plan cache information was returned.

When run on a sharded cluster, the operation returns plan cache entry information from a single member in each shard replica set. This member is identified with the `shard <plancachestats-shard>` and `host <plancachestats-host>` fields. See also `plancachestats-read-pref`.
