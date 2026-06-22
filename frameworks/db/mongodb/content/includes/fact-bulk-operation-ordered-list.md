---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bulk-operation-ordered-list.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When executing an :method:`ordered <db.collection.initializeOrderedBulkOp()>` list of operations, MongoDB groups the operations by the `operation type <batchType>` and contiguity; i.e. contiguous operations of the same type are grouped together. For example, if an ordered list has two insert operations followed by an update operation followed by another insert operation, MongoDB groups the operations into three separate groups: first group contains the two insert operations, second group contains the update operation, and the third group contains the last insert operation. This behavior is subject to change in future versions.
