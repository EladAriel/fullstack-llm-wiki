---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-insert-id-field.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** Most MongoDB driver clients include the `_id` field and
generate an `ObjectId` before sending the insert operation to
MongoDB. However, if the client sends a document without an `_id`
field, the :binary:`~bin.mongod adds the id` field and generates
the `ObjectId`.
