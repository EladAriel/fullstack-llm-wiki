---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/disk-spilling-metrics-overview.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

|disk-spilling-intro| contain new metrics if the query execution writes temporary files to disk. These metrics are prefixed by the query execution stage that caused the query to exceed the memory limit. For example, `sortSpills` indicates the number of times that the sort stage of query execution wrote temporary files to disk.
