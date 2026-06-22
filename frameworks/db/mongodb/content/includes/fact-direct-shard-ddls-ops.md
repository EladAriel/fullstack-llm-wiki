---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-direct-shard-ddls-ops.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.3, you can only run `DDL operations <ddl-operations>` and :dbcommand:`applyOps` on a `mongos` for all sharded clusters. These operations may be temporarily unavailable while transitioning from a replica set to a sharded cluster.
