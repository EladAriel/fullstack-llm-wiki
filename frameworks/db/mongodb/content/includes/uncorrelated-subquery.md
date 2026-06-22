---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/uncorrelated-subquery.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, for an uncorrelated subquery in a :pipeline:`$lookup` pipeline stage containing a :pipeline:`$sample` stage, the :expression:`$sampleRate` operator, or the :expression:`$rand` operator, the subquery is always run again if repeated. Previously, depending on the subquery output size, either the subquery output was cached or the subquery was run again.
