---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/refine-shard-key-index-type.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** Do not modify the range or hashed type for any of the current shard
key fields. It causes data inconsistencies. For example, do not
modify a shard key from `{ customer_id: 1 }` to ``{ customer_id:
"hashed", order_id: 1 }``.
