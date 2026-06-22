---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-bucket-max-span-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. The maximum time span between measurements in a bucket. For more information, see `flexible-bucketing`.

If you set this parameter:

- `timeseries.bucketRoundingSeconds` must have the same value.
- You can't set `timeseries.granularity`.
