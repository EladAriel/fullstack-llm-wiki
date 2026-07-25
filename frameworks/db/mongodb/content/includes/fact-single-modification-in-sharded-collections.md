---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-single-modification-in-sharded-collections.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To use |single-modification-operation-names| operations for a sharded collection that specify the |single-modification-operation-option| option:

- If you only target one shard, you can use a partial shard key in the query specification or,
- You can provide the `shard key or the id` field in the query
specification.
