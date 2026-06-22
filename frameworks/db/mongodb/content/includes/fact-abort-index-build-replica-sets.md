---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-abort-index-build-replica-sets.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For replica sets or shard replica sets, aborting an index on the primary does not simultaneously abort secondary index builds. MongoDB attempts to abort the in-progress builds for the specified indexes on the `primary` and if successful creates an associated `abort` `oplog` entry. `Secondary <secondary>` members with replicated in-progress builds wait for a commit or abort oplog entry from the primary before either committing or aborting the index build.
