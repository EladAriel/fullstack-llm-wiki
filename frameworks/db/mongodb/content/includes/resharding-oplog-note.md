---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/resharding-oplog-note.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:**  A |operation| operation is a write-intensive process which
 can generate increased rates of oplog. You may wish to:
 - set a fixed oplog size to prevent unbounded oplog growth.
 - increase the oplog size to minimize the chance that one or more
   secondary nodes becomes stale.
 See the `replica-set-oplog` documentation for more details.
