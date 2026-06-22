---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-meta-field-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. The name of the field which contains metadata in each time series document. The metadata in the specified field should be data that is used to label a unique series of documents. The metadata should rarely, if ever, change The name of the specified field may not be `_id` or the same as the `timeseries.timeField`. The field can be of any data type.

Although the `metaField` field is optional, using metadata can improve query optimization. For example, MongoDB automatically `creates a compound index <timeseries-add-secondary-index>` on the `metaField` and `timeField` fields for new collections. If you do not provide a value for this field, the data is bucketed solely based on time.
