---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bulk-operation-unordered-list.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When executing an :method:`unordered <db.collection.initializeUnorderedBulkOp()>` list of operations, MongoDB groups the operations. With an unordered bulk operation, the operations in the list may be reordered to increase performance. As such, applications should not depend on the ordering when performing :method:`unordered <db.collection.initializeUnorderedBulkOp()>` bulk operations.
