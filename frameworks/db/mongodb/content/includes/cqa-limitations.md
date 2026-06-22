---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cqa-limitations.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
