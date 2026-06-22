---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-read-and-write-distribution-metrics.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To return read and write distribution metrics for a collection using :dbcommand:`analyzeShardKey`, you must configure the query analyzer to sample the queries run on the collection. Otherwise, `analyzeShardKey` returns the read and write distribution metrics as `0` values. To configure the query analyzer, see `configureQueryAnalyzer`.
