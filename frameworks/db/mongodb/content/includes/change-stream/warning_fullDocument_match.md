---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/warning_fullDocument_match.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
