---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-secondary-index.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================

# Add Secondary Indexes to Time Series Collections

To improve query performance for `time series collections <time series collection>`, add one or more `secondary indexes <secondary index>` to support common time series query patterns. Starting in MongoDB 6.3, MongoDB automatically creates a `compound index <index-type-compound>` on the `metaField` and `timeField` fields for new collections.

> **Note:** Not all index types are supported. For a list of unsupported index
types, see :ref:`Limitations for Secondary Indexes on Time Series
Collections <timeseries-limitations-secondary-indexes>`.
