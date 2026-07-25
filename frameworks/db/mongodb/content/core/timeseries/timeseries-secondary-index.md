---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-secondary-index.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================================

# Add Secondary Indexes to Time Series Collections

To improve query performance for `time series collections <time series collection>`, add one or more `secondary indexes <secondary index>` to support common time series query patterns. Starting in MongoDB 6.3, MongoDB automatically creates a `compound index <index-type-compound>` on the `metaField` and `timeField` fields for new collections.

> **Note:** Not all index types are supported. For a list of unsupported index
types, see :ref:`Limitations for Secondary Indexes on Time Series
Collections <timeseries-limitations-secondary-indexes>`.
