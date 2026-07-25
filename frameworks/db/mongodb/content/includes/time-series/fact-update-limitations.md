---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-update-limitations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- You can only match on the `metaField` field value.
- You can only modify the `metaField` field value.
- Your update document can only contain :ref:`update operator
<update-operators>` expressions.

- Your update command must not limit the number of documents to be
updated. Set `multi: true` or use the :method:`~db.collection.updateMany()` method.

- Your update command must not set `upsert: true <update-upsert>`.
