---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-index-build-memory-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The :parameter:`maxIndexBuildMemoryUsageMegabytes` limit applies to all index builds initiated by user commands like :dbcommand:`createIndexes` or administrative processes like `initial sync <replica-set-sync>`.

An `initial sync <replica-set-sync>` populates only one collection at a time and has no risk of exceeding the memory limit. However, it is possible for a user to start index builds on multiple collections in multiple databases simultaneously.
