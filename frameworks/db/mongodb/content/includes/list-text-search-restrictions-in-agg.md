---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-text-search-restrictions-in-agg.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- The :pipeline:`$match` stage that includes a `$text` must be
the **first** stage in the pipeline.

- A `$text` operator can only occur once in the stage.
- The `$text` operator expression cannot appear in
:expression:`$or` or :expression:`$not` expressions.

- `$text`, by default, does not return the matching documents in order
of matching scores. To sort by descending score, use the :expression:`$meta` aggregation expression in the :pipeline:`$sort` stage.
