---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/fullDocument-postimage.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. versionchanged:: 6.0

Starting in MongoDB 6.0, if you set the `changeStreamPreAndPostImages` option using :method:`db.createCollection()`, :dbcommand:`create`, or :dbcommand:`collMod`, then the `fullDocument` field shows the document after it was inserted, replaced, or updated (the document post-image). `fullDocument` is always included for `insert` events.
