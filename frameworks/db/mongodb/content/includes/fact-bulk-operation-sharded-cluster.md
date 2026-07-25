---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bulk-operation-sharded-cluster.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Executing an :method:`ordered <db.collection.initializeOrderedBulkOp()>` list of operations on a sharded collection will generally be slower than executing an :method:`unordered <db.collection.initializeUnorderedBulkOp()>` list since with an ordered list, each operation must wait for the previous operation to finish.
