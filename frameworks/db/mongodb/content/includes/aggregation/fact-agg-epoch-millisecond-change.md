---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/fact-agg-epoch-millisecond-change.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:gold:`IMPORTANT:` Starting in MongoDB 8.3, if `unit` is not `"millisecond"` and the input date is before `ISODate("1970-01-01T00:00:00Z")`, the result is one second greater than in previous versions of MongoDB.
