---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-no-shard-after-demotion.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.3, replica sets that were previously sharded clusters cannot be converted back into replica sets.

The conversion of a sharded cluster into a replica set preserves sharding metadata from its prior deployment, including a shard identity document, which blocks it from again becoming a sharded cluster. If you attempt a self-managed conversion back into a sharded cluster, MongoDB returns an error.

To convert such replica sets into sharded clusters, contact `technical-support`.
