---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/long-running-secondary-reads-may-terminate.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** Starting in MongoDB version 8.2, long-running secondary reads in a
sharded cluster may automatically terminate before orphaned document
deletion following a chunk migration.
The :parameter:`terminateSecondaryReadsOnOrphanCleanup` parameter
controls this behavior. To learn more about handling long-running
secondary reads, see `long-running-secondary-reads`.
