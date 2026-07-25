---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-index-build-memory-limit.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The :parameter:`maxIndexBuildMemoryUsageMegabytes` limit applies to all index builds initiated by user commands like :dbcommand:`createIndexes` or administrative processes like `initial sync <replica-set-sync>`.

An `initial sync <replica-set-sync>` populates only one collection at a time and has no risk of exceeding the memory limit. However, it is possible for a user to start index builds on multiple collections in multiple databases simultaneously.
