---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-text-search-restrictions-in-agg.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- The :pipeline:`$match` stage that includes a `$text` must be
the **first** stage in the pipeline.

- A `$text` operator can only occur once in the stage.
- The `$text` operator expression cannot appear in
:expression:`$or` or :expression:`$not` expressions.

- `$text`, by default, does not return the matching documents in order
of matching scores. To sort by descending score, use the :expression:`$meta` aggregation expression in the :pipeline:`$sort` stage.
