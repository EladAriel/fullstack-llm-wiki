---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/fact-type-of-operation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In a `$group` stage, |operatorName| is an accumulator and calculates a value for all documents in the window.

In a `$project` stage, |operatorName| is an aggregation expression and calculates values for each document.

In `$setWindowFields` stages, |operatorName| returns a result for each document like an aggregation expression, but the results are computed over groups of documents like an accumulator.
