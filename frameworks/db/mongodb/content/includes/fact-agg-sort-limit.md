---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-agg-sort-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When a :pipeline:`$sort` precedes a :pipeline:`$limit` and there are no intervening stages that modify the number of documents, the optimizer can coalesce the :pipeline:`$limit` into the :pipeline:`$sort`. This allows the :pipeline:`$sort` operation to only maintain the top `n` results as it progresses, where `n` is the specified limit, and ensures that MongoDB only needs to store `n` items in memory. This optimization still applies when `allowDiskUse` is `true` and the `n` items exceed the `aggregation memory limit <agg-memory-restrictions>`.
