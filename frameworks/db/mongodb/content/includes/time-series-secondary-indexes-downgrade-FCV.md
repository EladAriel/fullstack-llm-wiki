---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series-secondary-indexes-downgrade-FCV.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If there are `secondary indexes <secondary index>` on `time series collections <manual-timeseries-collection>` and you need to downgrade the feature compatibility version (FCV), you must first drop any secondary indexes that are incompatible with the downgraded FCV. For more information, see :dbcommand:`setFeatureCompatibilityVersion`.
