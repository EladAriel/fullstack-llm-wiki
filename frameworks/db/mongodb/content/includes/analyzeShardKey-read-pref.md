---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-read-pref.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To minimize the performance, run |analyzeShardKey| with the :readmode:`secondary` or :readmode:`secondaryPreferred` read preference. On a sharded cluster, `mongos` automatically sets the read preference to `secondaryPreferred` if not specified.
