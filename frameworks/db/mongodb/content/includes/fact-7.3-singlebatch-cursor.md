---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-7.3-singlebatch-cursor.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 7.3, when you use a find command on a view with the `singleBatch: true` and `batchSize: 1` options, a cursor is no longer returned. In previous versions of MongoDB these find queries would return a cursor even when you set the `single batch<find-single-batch>` option to `true`.
