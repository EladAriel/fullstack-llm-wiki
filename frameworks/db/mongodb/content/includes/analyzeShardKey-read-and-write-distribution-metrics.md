---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-read-and-write-distribution-metrics.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To return read and write distribution metrics for a collection using :dbcommand:`analyzeShardKey`, you must configure the query analyzer to sample the queries run on the collection. Otherwise, `analyzeShardKey` returns the read and write distribution metrics as `0` values. To configure the query analyzer, see `configureQueryAnalyzer`.
