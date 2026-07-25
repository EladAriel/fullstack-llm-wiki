---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-bucket-rounding-description.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. The time interval that determines the starting timestamp for a new bucket. For more information, see `flexible-bucketing`.

If you set this parameter:

- `timeseries.bucketMaxSpanSeconds` must have the same value.
- You can't set `timeseries.granularity`.
