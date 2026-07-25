---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/shard-key-read-write-distribution.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

`readWriteDistribution` contains metrics about the query routing patterns and the `hotness <sharding-troubleshooting-monotonicity>` of shard key ranges. These metrics are based on sampled queries.

To configure query sampling for a collection, use the `configureQueryAnalyzer` command. The read and write distribution metrics are only returned if `readWriteDistribution` is `true`. The metrics are calculated when |analyzeShardKey| is run and the metrics use the sampled read and write queries. If there are no sampled queries, read and write distribution metrics aren't returned.

- If there are no sampled read queries, the command returns
`writeDistribution` but omits `readDistribution`.

- If there are no sampled write queries, the command returns
`readDistribution` but omits `writeDistribution`.

.. include:: /includes/analyzeShardKey-read-and-write-distribution-metrics.rst
