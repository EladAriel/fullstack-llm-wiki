---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-update-field-order.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For write operations, MongoDB preserves the order of the document fields except for the following cases:

- The `_id` field is always the first field in the document.
- Updates that include :update:`renaming <$rename>` of field names may
result in the reordering of fields in the document.
