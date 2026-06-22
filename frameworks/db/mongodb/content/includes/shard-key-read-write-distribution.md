---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/shard-key-read-write-distribution.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`readWriteDistribution` contains metrics about the query routing patterns and the `hotness <sharding-troubleshooting-monotonicity>` of shard key ranges. These metrics are based on sampled queries.

To configure query sampling for a collection, use the `configureQueryAnalyzer` command. The read and write distribution metrics are only returned if `readWriteDistribution` is `true`. The metrics are calculated when |analyzeShardKey| is run and the metrics use the sampled read and write queries. If there are no sampled queries, read and write distribution metrics aren't returned.

- If there are no sampled read queries, the command returns
`writeDistribution` but omits `readDistribution`.

- If there are no sampled write queries, the command returns
`readDistribution` but omits `writeDistribution`.

.. include:: /includes/analyzeShardKey-read-and-write-distribution-metrics.rst
