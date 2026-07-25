---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.1-fassert-shard-restart-add-CWWC.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.1, when starting, restarting or adding a `shard server <sharding-shards>` with :method:`sh.addShard()` the `Cluster Wide Write Concern (CWWC) <set_global_default_write_concern>` must be set.

If the `CWWC` is not set and the shard is configured such that the `default write concern <write-concern>` is `{ w : 1 }` the shard server will fail to start or be added and returns an error.

See `default write concern calculations <default-wc-formula>` for details on how the default write concern is calculated.
