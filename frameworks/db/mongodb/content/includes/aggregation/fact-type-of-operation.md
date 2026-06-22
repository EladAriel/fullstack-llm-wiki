---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/fact-type-of-operation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In a `$group` stage, |operatorName| is an accumulator and calculates a value for all documents in the window.

In a `$project` stage, |operatorName| is an aggregation expression and calculates values for each document.

In `$setWindowFields` stages, |operatorName| returns a result for each document like an aggregation expression, but the results are computed over groups of documents like an accumulator.
