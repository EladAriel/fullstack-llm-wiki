---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/blocking-performance.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

|stage| is a blocking stage, which causes the pipeline to wait for all input data to be retrieved for the blocking stage before processing the data. A blocking stage may reduce performance because it reduces parallel processing for a pipeline with multiple stages. A blocking stage may also use substantial amounts of memory for large data sets.
