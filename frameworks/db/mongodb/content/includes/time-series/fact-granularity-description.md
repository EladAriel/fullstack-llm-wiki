---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-granularity-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. Possible values are:

- `"seconds"`
- `"minutes"`
- `"hours"`
By default, MongoDB sets the `granularity` to `"seconds"` for high-frequency ingestion.

Manually set the `granularity` parameter to improve performance by optimizing how data in the time series collection is stored internally. To select a value for `granularity`, choose the closest match to the time span between consecutive incoming measurements.

If you specify the `timeseries.metaField`, consider the time span between consecutive incoming measurements that have the same unique value for the `metaField` field. Measurements often have the same unique value for the `metaField` field if they come from the same source.

If you do not specify `timeseries.metaField`, consider the time span between all measurements that are inserted in the collection.

If you set the `granularity` parameter, you can't set the `bucketMaxSpanSeconds` and `bucketRoundingSeconds` parameters.
