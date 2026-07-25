---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-abort-index-build-replica-sets.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For replica sets or shard replica sets, aborting an index on the primary does not simultaneously abort secondary index builds. MongoDB attempts to abort the in-progress builds for the specified indexes on the `primary` and if successful creates an associated `abort` `oplog` entry. `Secondary <secondary>` members with replicated in-progress builds wait for a commit or abort oplog entry from the primary before either committing or aborting the index build.
