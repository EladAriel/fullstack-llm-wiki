---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/fact-behavior-percent-median.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can use |operatorName| in:

- :pipeline:`$group <$group>` stages as an accumulator
- :pipeline:`$setWindowFields` stages as an accumulator
- :pipeline:`$project <$project>` stages as an aggregation expression
|operatorName| has the following characteristics as an accumulator, it:

- Calculates a single result for all the documents in the stage.
- Uses the [t-digest](https://arxiv.org/abs/1902.04023)_ algorithm to
calculate approximate, percentile based metrics.

- Uses approximate methods to scale to large volumes of data.
|operatorName| has the following characteristics as an aggregation expression, it:

- Accepts an array as input
- Calculates a separate result for each input document
