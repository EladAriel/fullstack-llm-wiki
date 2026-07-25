---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/equivalent-indexes.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 7.3, you cannot create equivalent indexes, which are partial indexes with the same index keys and the same partial expressions that use a `collation <collation>`.

For databases in MongoDB 7.3 with existing equivalent indexes, the indexes are retained but only the first equivalent index is used in queries. This is the same behavior as MongoDB versions earlier than 7.3.
