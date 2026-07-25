---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-id-field-name-rules.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The field name `_id is reserved for use as a primary key; its value must be unique in the collection, is immutable, and may be of any type other than an array or regex. If the id` contains subfields, the subfield names cannot begin with a (`$`) symbol.
