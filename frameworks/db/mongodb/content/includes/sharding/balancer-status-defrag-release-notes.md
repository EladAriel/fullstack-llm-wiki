---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharding/balancer-status-defrag-release-notes.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.3, the :dbcommand:`balancerCollectionStatus` command returns detailed information when run on a namespace going through chunk defragmentation. The output includes the current phase of the defragmentation and how many chunks are left to process.

To see example output, see `balancer-collection-status-defrag-output-command`.
