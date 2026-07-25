---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/fullDocument-postimage.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. versionchanged:: 6.0

Starting in MongoDB 6.0, if you set the `changeStreamPreAndPostImages` option using :method:`db.createCollection()`, :dbcommand:`create`, or :dbcommand:`collMod`, then the `fullDocument` field shows the document after it was inserted, replaced, or updated (the document post-image). `fullDocument` is always included for `insert` events.
