---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-document-field-name-restrictions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- Field names **cannot** contain the `null` character.
- The server permits storage of field names that contain dots (`.`)
and dollar signs (`$`).

- MongodB 5.0 adds improved support for the use of (`$`) and (`.`)
in field names. There are some restrictions. See `Field Name Considerations <crud-concepts-dot-dollar-considerations>` for more details.

- Each field name must be unique within the document. You must not store
documents with duplicate fields because MongoDB `CRUD <crud>` operations might behave unexpectedly if a document has duplicate fields.
