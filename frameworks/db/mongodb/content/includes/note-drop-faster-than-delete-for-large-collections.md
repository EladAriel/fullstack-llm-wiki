---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-drop-faster-than-delete-for-large-collections.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** If you are deleting all documents in a large collection, it may be faster
to drop the collection and recreate it. Before dropping the collection,
note all indexes on the collection. You must recreate any
`indexes <manual-create-an-index>` that existed in the original
collection. If the original collection was sharded, you must also
`shard <sharding-shard-key-creation>` the recreated collection.
For more information on dropping a collection, see
:method:`db.collection.drop()`.
