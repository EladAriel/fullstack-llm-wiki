---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-multiple-partial-index.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, multiple `partial indexes <index-type-partial>` can be created using the same `key pattern<key_patterns>` as long as the `partialFilterExpression <partialFilterExpression>` fields do not express equivalent filters.

In earlier versions of MongoDB, creating multiple `partial indexes <index-type-partial>` is not allowed when using the same key pattern with different `partialFilterExpressions <partialFilterExpression>`.
