---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-update-limitations.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- You can only match on the `metaField` field value.
- You can only modify the `metaField` field value.
- Your update document can only contain :ref:`update operator
<update-operators>` expressions.

- Your update command must not limit the number of documents to be
updated. Set `multi: true` or use the :method:`~db.collection.updateMany()` method.

- Your update command must not set `upsert: true <update-upsert>`.
