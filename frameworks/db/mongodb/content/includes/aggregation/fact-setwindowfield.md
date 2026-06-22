---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/fact-setwindowfield.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A window function lets you calculate results over a moving "window" of neighboring documents. As each document passes though the pipeline, the :pipeline:`$setWindowFields` stage:

- Recomputes the set of documents in the current window
- calculates a value for all documents in the set
- returns a single value for that document
You can use |operatorName| in a `$setWindowFields` stage to calculate rolling statistics for `time series <manual-timeseries-landing>` or other related data.

When you use |operatorName| in a `$setWindowField` stage, the `input` value must be a field name. If you enter an array instead of a field name, the operation fails.
