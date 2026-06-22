---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bulk-operation-batches.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:method:`Bulk()` operations in :binary:`~bin.mongosh` and comparable methods in the drivers do not have a limit for the number of operations in a group. To see how the operations are grouped for bulk operation execution, call :method:`Bulk.getOperations()` after the execution.

> **Seealso:** - :limit:`Write Command Batch Limit Size`
