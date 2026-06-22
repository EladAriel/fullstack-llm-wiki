---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-timeseries-param-desc.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. Specify this option to create a new sharded `time series collection <manual-timeseries-collection>`.

To shard an existing time series collection, omit this parameter.

When the collection specified to `shardCollection` is a time series collection and the `timeseries` option is not specified, MongoDB uses the values that define the existing time series collection to populate the `timeseries` field.
