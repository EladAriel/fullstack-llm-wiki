---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/disk-spilling-metrics-overview.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

|disk-spilling-intro| contain new metrics if the query execution writes temporary files to disk. These metrics are prefixed by the query execution stage that caused the query to exceed the memory limit. For example, `sortSpills` indicates the number of times that the sort stage of query execution wrote temporary files to disk.
