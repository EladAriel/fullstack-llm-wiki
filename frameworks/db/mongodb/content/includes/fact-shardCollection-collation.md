---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-shardCollection-collation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Collation

If the collection has a default `collation <collation>`, the |command| command must include a `collation` parameter with the value `{ locale: "simple" }`. For non-empty collections with a default collation, you must have at least one index with the simple collation whose fields support the shard key pattern.

You do not need to specify the `collation` option for collections without a collation. If you do specify the collation option for a collection with no collation, it will have no effect.
