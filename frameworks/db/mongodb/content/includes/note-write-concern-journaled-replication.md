---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-write-concern-journaled-replication.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

With :writeconcern:`j: true <j>`, MongoDB returns only after the requested number of members, including the primary, have written to the journal. Previously :writeconcern:`j: true <j>` write concern in a replica set only requires the `primary` to write to the journal, regardless of the `w: \<value\> <wc-w>` write concern.
