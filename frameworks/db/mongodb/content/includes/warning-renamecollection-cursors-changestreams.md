---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-renamecollection-cursors-changestreams.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** The :method:`db.collection.renameCollection()` method and
:dbcommand:`renameCollection` command invalidate open cursors. This creates
an `invalidate event <change-event-invalidate>` for any existing
`change streams <changeStreams>` opened on the source or target
collection, and also interrupts queries that are currently returning
data from the renamed collection.
