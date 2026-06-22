---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/exist-op-support-expressions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** `Expressions <aggregation-expressions>` do not support
the :query:`$exists` operator. To check for the existence of a field in an
expression, you can use the :expression:`$type` aggregation
operator to check if a field has a type of `missing`.
For more information, see `$type Existence Check <missing-type-existence-check>`.
