---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-id-field-name-rules.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The field name `_id is reserved for use as a primary key; its value must be unique in the collection, is immutable, and may be of any type other than an array or regex. If the id` contains subfields, the subfield names cannot begin with a (`$`) symbol.
