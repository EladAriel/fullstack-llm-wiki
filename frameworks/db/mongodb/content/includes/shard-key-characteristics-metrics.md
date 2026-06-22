---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/shard-key-characteristics-metrics.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`keyCharacteristic` consists of the metrics about the `cardinality <sharding-shard-key-cardinality>`, `frequency <shard-key-frequency>`, and `monotonicity <shard-key-monotonic>` of the shard key. These metrics are only returned when `keyCharacteristics` is true.

The metrics are calculated when |analyzeShardKey| is run based on documents sampled from the collection. The calculation requires the shard key to have a `supporting index <supporting-indexes-ref>`. If there is no supporting index, no metrics are returned.

You can configure sampling with the `sampleRate` and `sampleSize` fields. Both are optional, but only one can be specified. When both `sampleRate` and `sampleSize` are unspecified, MongoDB uses the value of the :parameter:`analyzeShardKeyCharacteristicsDefaultSampleSize` parameter, which has a default value of 10 million.

To calculate metrics based on all documents in the collection, set the `sampleRate` to `1`.
