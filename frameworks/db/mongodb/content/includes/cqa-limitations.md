---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cqa-limitations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- You cannot run |CQA| on Atlas
`flex clusters <flex--cluster>`.

- You cannot run |CQA| on
standalone deployments.

- You cannot run |CQA| directly
against a :option:`--shardsvr <mongod --shardsvr>` replica set. When running on a sharded cluster, |CQA| must run against a `mongos`.

- You cannot run |CQA| against
`time series <cmd-shard-collection-timeseries>` collections.

- You cannot run |CQA| against
collections with `Queryable Encryption <qe-manual-feature-qe>`.
