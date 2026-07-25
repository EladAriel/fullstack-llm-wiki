---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/uncorrelated-subquery.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, for an uncorrelated subquery in a :pipeline:`$lookup` pipeline stage containing a :pipeline:`$sample` stage, the :expression:`$sampleRate` operator, or the :expression:`$rand` operator, the subquery is always run again if repeated. Previously, depending on the subquery output size, either the subquery output was cached or the subquery was run again.
