---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/exist-op-support-expressions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** `Expressions <aggregation-expressions>` do not support
the :query:`$exists` operator. To check for the existence of a field in an
expression, you can use the :expression:`$type` aggregation
operator to check if a field has a type of `missing`.
For more information, see `$type Existence Check <missing-type-existence-check>`.
