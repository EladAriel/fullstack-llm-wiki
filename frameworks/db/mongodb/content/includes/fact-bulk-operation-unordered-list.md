---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bulk-operation-unordered-list.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When executing an :method:`unordered <db.collection.initializeUnorderedBulkOp()>` list of operations, MongoDB groups the operations. With an unordered bulk operation, the operations in the list may be reordered to increase performance. As such, applications should not depend on the ordering when performing :method:`unordered <db.collection.initializeUnorderedBulkOp()>` bulk operations.
