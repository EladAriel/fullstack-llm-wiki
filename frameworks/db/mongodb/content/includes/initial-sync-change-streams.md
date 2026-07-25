---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/initial-sync-change-streams.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If the :parameter:`initialSyncMethod` parameter for the cluster is `fileCopyBased`, then there is no impact on change stream listeners.

If `initialSyncMethod` is `logical` and a change stream is opened on a newly synchronized node and reads events from a point in time earlier than the completion of the logical initial sync, the pre- and post-images may be missing.
