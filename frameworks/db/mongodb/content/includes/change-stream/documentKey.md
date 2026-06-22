---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/documentKey.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Document that contains the `_id` value of the document created or modified by the `CRUD <crud>` operation.

For sharded collections, this field also displays the full shard key for the document. The `_id` field is not repeated if it is already a part of the shard key.
