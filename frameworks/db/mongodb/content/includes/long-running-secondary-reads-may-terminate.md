---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/long-running-secondary-reads-may-terminate.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** Starting in MongoDB version 8.2, long-running secondary reads in a
sharded cluster may automatically terminate before orphaned document
deletion following a chunk migration.
The :parameter:`terminateSecondaryReadsOnOrphanCleanup` parameter
controls this behavior. To learn more about handling long-running
secondary reads, see `long-running-secondary-reads`.
