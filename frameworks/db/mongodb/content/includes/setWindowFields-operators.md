---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/setWindowFields-operators.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

These operators can be used with the :pipeline:`$setWindowFields` stage:

- Accumulator operators: :group:`$addToSet`, :group:`$avg`,
:group:`$bottom`, :group:`$bottomN`, :group:`$concatArrays`, :group:`$count`, :group:`$covariancePop`, :group:`$covarianceSamp`, :group:`$derivative`, :group:`$expMovingAvg`, :group:`$firstN`, :group:`$integral`, :group:`$lastN`, :group:`$max`, :group:`$maxN`, :group:`$median`, :expression:`$mergeObjects`, :group:`$min`, :group:`$minN`, :group:`$percentile`, :group:`$push`, :group:`$setUnion`, :group:`$stdDevSamp`, :group:`$stdDevPop`, :group:`$sum`, :group:`$top`, :group:`$topN`.

- Gap filling operators: :group:`$linearFill` and :group:`$locf`.
- Order operators: :group:`$first`, :group:`$last`, and :group:`$shift`.
- Rank operators: :group:`$denseRank`, :group:`$documentNumber`, and
:group:`$rank`.

- Range operator: :group:`$minMaxScaler`
