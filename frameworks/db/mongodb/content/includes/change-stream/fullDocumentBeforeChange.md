---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/fullDocumentBeforeChange.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The document before changes were applied by the operation. That is, the document pre-image.

This field is available when you enable the `changeStreamPreAndPostImages` field for a collection using :method:`db.createCollection()` method or the :dbcommand:`create` or :dbcommand:`collMod` commands.

.. versionadded:: 6.0
