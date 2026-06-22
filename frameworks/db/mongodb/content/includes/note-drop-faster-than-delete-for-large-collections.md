---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-drop-faster-than-delete-for-large-collections.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** If you are deleting all documents in a large collection, it may be faster
to drop the collection and recreate it. Before dropping the collection,
note all indexes on the collection. You must recreate any
`indexes <manual-create-an-index>` that existed in the original
collection. If the original collection was sharded, you must also
`shard <sharding-shard-key-creation>` the recreated collection.
For more information on dropping a collection, see
:method:`db.collection.drop()`.
