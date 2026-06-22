---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/set-aggregation-versus-update.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In this pipeline, `$set` and `$unset` are aggregation stages, as opposed to update operators. The aggregation stages :pipeline:`$set` and :pipeline:`$unset` add new fields to documents and do not modify existing field values.

For more information on the update operators, see :update:`$set` and :update:`$unset`.
