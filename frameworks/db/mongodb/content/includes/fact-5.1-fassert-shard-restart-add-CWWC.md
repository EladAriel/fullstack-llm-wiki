---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.1-fassert-shard-restart-add-CWWC.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.1, when starting, restarting or adding a `shard server <sharding-shards>` with :method:`sh.addShard()` the `Cluster Wide Write Concern (CWWC) <set_global_default_write_concern>` must be set.

If the `CWWC` is not set and the shard is configured such that the `default write concern <write-concern>` is `{ w : 1 }` the shard server will fail to start or be added and returns an error.

See `default write concern calculations <default-wc-formula>` for details on how the default write concern is calculated.
