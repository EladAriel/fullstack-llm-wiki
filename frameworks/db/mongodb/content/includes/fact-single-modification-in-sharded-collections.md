---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-single-modification-in-sharded-collections.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To use |single-modification-operation-names| operations for a sharded collection that specify the |single-modification-operation-option| option:

- If you only target one shard, you can use a partial shard key in the query specification or,
- You can provide the `shard key or the id` field in the query
specification.
