---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-shardCollection-collation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Collation

If the collection has a default `collation <collation>`, the |command| command must include a `collation` parameter with the value `{ locale: "simple" }`. For non-empty collections with a default collation, you must have at least one index with the simple collation whose fields support the shard key pattern.

You do not need to specify the `collation` option for collections without a collation. If you do specify the collation option for a collection with no collation, it will have no effect.
