---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-multiple-partial-index.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, multiple `partial indexes <index-type-partial>` can be created using the same `key pattern<key_patterns>` as long as the `partialFilterExpression <partialFilterExpression>` fields do not express equivalent filters.

In earlier versions of MongoDB, creating multiple `partial indexes <index-type-partial>` is not allowed when using the same key pattern with different `partialFilterExpressions <partialFilterExpression>`.
