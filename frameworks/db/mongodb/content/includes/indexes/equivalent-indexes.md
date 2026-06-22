---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/equivalent-indexes.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 7.3, you cannot create equivalent indexes, which are partial indexes with the same index keys and the same partial expressions that use a `collation <collation>`.

For databases in MongoDB 7.3 with existing equivalent indexes, the indexes are retained but only the first equivalent index is used in queries. This is the same behavior as MongoDB versions earlier than 7.3.
