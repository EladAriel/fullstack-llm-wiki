---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-text-search-spilling.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.3, the query engine limits the `TextOr` stage memory usage to 100 megabytes. The `TextOr` stage processes :query:`$text` queries that read text score metadata. For example, `TextOr` processes queries that sort results by text score. If the `TextOr` stage exceeds this limit:

- If `allowDiskUse` is `true`, the stage spills intermediate
results to disk.

- If `allowDiskUse` is `false`, the query fails with an
exceeded memory limit error.

In earlier versions, the `TextOr` stage had no memory limit and consumed RAM without restrictions, risking out-of-memory (OOM) errors.
