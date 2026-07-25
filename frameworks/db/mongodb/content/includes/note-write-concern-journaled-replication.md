---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-write-concern-journaled-replication.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

With :writeconcern:`j: true <j>`, MongoDB returns only after the requested number of members, including the primary, have written to the journal. Previously :writeconcern:`j: true <j>` write concern in a replica set only requires the `primary` to write to the journal, regardless of the `w: \<value\> <wc-w>` write concern.
