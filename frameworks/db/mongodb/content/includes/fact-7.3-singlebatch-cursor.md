---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-7.3-singlebatch-cursor.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 7.3, when you use a find command on a view with the `singleBatch: true` and `batchSize: 1` options, a cursor is no longer returned. In previous versions of MongoDB these find queries would return a cursor even when you set the `single batch<find-single-batch>` option to `true`.
