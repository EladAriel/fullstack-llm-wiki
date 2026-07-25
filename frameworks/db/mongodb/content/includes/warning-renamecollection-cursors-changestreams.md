---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-renamecollection-cursors-changestreams.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** The :method:`db.collection.renameCollection()` method and
:dbcommand:`renameCollection` command invalidate open cursors. This creates
an `invalidate event <change-event-invalidate>` for any existing
`change streams <changeStreams>` opened on the source or target
collection, and also interrupts queries that are currently returning
data from the renamed collection.
