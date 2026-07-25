---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/documentKey.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Document that contains the `_id` value of the document created or modified by the `CRUD <crud>` operation.

For sharded collections, this field also displays the full shard key for the document. The `_id` field is not repeated if it is already a part of the shard key.
