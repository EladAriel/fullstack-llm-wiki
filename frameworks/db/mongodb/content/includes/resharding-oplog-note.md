---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/resharding-oplog-note.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:**  A |operation| operation is a write-intensive process which
 can generate increased rates of oplog. You may wish to:
 - set a fixed oplog size to prevent unbounded oplog growth.
 - increase the oplog size to minimize the chance that one or more
   secondary nodes becomes stale.
 See the `replica-set-oplog` documentation for more details.
