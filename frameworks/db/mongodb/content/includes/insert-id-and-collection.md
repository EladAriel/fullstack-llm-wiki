---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/insert-id-and-collection.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If the collection does not exist, then |method| creates the collection.

If the document to insert does not specify an `_id` field, then :binary:`~bin.mongod adds the id` field and assigns a unique :method:`ObjectId for the document. Most drivers create an ObjectId and insert the id` field, but the :binary:`~bin.mongod will create and populate the id` if the driver or application does not.

If the document contains an `_id field, the id` value must be unique within the collection to avoid duplicate key error.
