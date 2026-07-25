---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/set-aggregation-versus-update.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In this pipeline, `$set` and `$unset` are aggregation stages, as opposed to update operators. The aggregation stages :pipeline:`$set` and :pipeline:`$unset` add new fields to documents and do not modify existing field values.

For more information on the update operators, see :update:`$set` and :update:`$unset`.
