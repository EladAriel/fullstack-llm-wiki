---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/fact-granularity-field-description.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. Do not use if setting `bucketRoundingSeconds` and `bucketMaxSpanSeconds`.

Possible values are `seconds` (default), `minutes`, and `hours`.

Set `granularity` to the value that most closely matches the time between consecutive incoming timestamps. This improves performance by optimizing how MongoDB stores data in the collection.

For more information on granularity and bucket intervals, see `timeseries-granularity`.
