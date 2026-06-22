---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/primary-shard-enable-sharding-opt.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. The `primary shard <primary-shard>` for the database. It's the default shard for all unsharded collections in the database.

:red:`WARNING:` In general, you should **not** specify the primary shard. Allow the cluster to select the primary shard instead.
