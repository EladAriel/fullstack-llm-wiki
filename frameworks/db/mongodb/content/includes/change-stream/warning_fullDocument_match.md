---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/warning_fullDocument_match.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** For situations involving rapid deletions or traffic spikes, configuring
`fullDocument: "updateLookup"` with a :pipeline:`$match` filter can cause
'Resume Token Not Found' errors. This occurs when a document deletion causes
the `fullDocument` field to return a null value, because there is no
matching document, which then prevents the change stream from finding
the resume token.
Instead, use Pre- and Post-Images with ``fullDocumentBeforeChange:
"whenAvailable"` and `fullDocument: "whenAvailable"``. See the :ref:`Change Streams with Document Pre- and Post-Images
<db.collection.watch-change-streams-pre-and-post-images-example>` section.
