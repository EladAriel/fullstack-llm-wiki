---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/initial-sync-change-streams.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If the :parameter:`initialSyncMethod` parameter for the cluster is `fileCopyBased`, then there is no impact on change stream listeners.

If `initialSyncMethod` is `logical` and a change stream is opened on a newly synchronized node and reads events from a point in time earlier than the completion of the logical initial sync, the pre- and post-images may be missing.
