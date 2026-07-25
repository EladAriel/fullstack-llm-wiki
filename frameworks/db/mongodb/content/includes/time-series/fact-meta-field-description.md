---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-meta-field-description.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. The name of the field which contains metadata in each time series document. The metadata in the specified field should be data that is used to label a unique series of documents. The metadata should rarely, if ever, change The name of the specified field may not be `_id` or the same as the `timeseries.timeField`. The field can be of any data type.

Although the `metaField` field is optional, using metadata can improve query optimization. For example, MongoDB automatically `creates a compound index <timeseries-add-secondary-index>` on the `metaField` and `timeField` fields for new collections. If you do not provide a value for this field, the data is bucketed solely based on time.
