---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-upsert-id.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you execute an :method:`~db.collection.update()` with `upsert: true and the query matches no existing document, MongoDB will refuse to insert a new document if the query specifies conditions on the id` field using `dot notation <document-dot-notation>`.

This restriction ensures that the order of fields embedded in the `_id` document is well-defined and not bound to the order specified in the query.

If you attempt to insert a document in this way, MongoDB raises an error.
