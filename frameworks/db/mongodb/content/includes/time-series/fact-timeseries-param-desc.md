---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-timeseries-param-desc.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. Specify this option to create a new sharded `time series collection <manual-timeseries-collection>`.

To shard an existing time series collection, omit this parameter.

When the collection specified to `shardCollection` is a time series collection and the `timeseries` option is not specified, MongoDB uses the values that define the existing time series collection to populate the `timeseries` field.
