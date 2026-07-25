---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-no-shard-after-demotion.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.3, replica sets that were previously sharded clusters cannot be converted back into replica sets.

The conversion of a sharded cluster into a replica set preserves sharding metadata from its prior deployment, including a shard identity document, which blocks it from again becoming a sharded cluster. If you attempt a self-managed conversion back into a sharded cluster, MongoDB returns an error.

To convert such replica sets into sharded clusters, contact `technical-support`.
