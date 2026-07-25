---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/shard-key-analyzer-info.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in 7.0, MongoDB makes it easier to choose your shard key. You can use :dbcommand:`analyzeShardKey` which calculates metrics for evaluating a shard key for an unsharded or sharded collection. Metrics are based on sampled queries, allowing you to make a data-driven choice for your shard key.

### Enable Query Sampling

To analyze a shard key, you must enable query sampling on the target collection. For more information, see:

- :dbcommand:`configureQueryAnalyzer` database command
- :method:`db.collection.configureQueryAnalyzer()` shell method
To monitor the query sampling process, use the :pipeline:`$currentOp` stage. For an example, see `sampled-queries-currentOp-stage`.

### Shard Key Analysis Commands

To analyze a shard key, see:

- :dbcommand:`analyzeShardKey` database command
- :method:`db.collection.analyzeShardKey()` shell method
`analyzeShardKey` returns metrics about key characteristics of a shard key and its read and write distribution. The metrics are based on sampled queries.

- The `keyCharacteristics` field contains metrics about the
`cardinality <shard-key-cardinality>`, `frequency <shard-key-frequency>`, and `monotonicity <shard-key-monotonic>` of the shard key.

- The `readWriteDistribution` field contains :ref:`metrics
<read-write-distribution-output>` about the query routing patterns and the load distribution of shard key ranges.

> **Seealso:** - `read-operations-sharded-clusters`
- `sharding-query-router-broadcast-targeted`
