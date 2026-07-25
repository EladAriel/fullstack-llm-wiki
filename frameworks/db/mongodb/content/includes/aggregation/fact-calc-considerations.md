---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/fact-calc-considerations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In `$group` stages, |operatorName| always uses an approximate calculation method.

In `$project` stages, |operatorName| might use the discrete calculation method even when the approximate method is specified.

In `$setWindowFields` stages, the workload determines the calculation method that |operatorName| uses.

The computed percentiles |operatorName| returns might vary, even on the same datasets. This is because the algorithm calculates approximate values.

Duplicate samples can cause ambiguity. If there are a large number of duplicates, the percentile values may not represent the actual sample distribution. Consider a data set where all the samples are the same. All of the values in the data set fall at or below any percentile. A "50th percentile" value would actually represent either 0 or 100 percent of the samples.
