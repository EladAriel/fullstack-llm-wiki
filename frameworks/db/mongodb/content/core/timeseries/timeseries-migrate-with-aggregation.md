---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-migrate-with-aggregation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================================

# Migrate Data into a Time Series Collection with Aggregation

Starting in MongoDB version 7.0, you can use the :pipeline:`$out` aggregation stage to migrate data from an existing collection into a `time series collection <manual-timeseries-collection>`.

> **Note:** MongoDB does not guarantee output order when you use :pipeline:`$out` to
migrate data into a times series collection. To maintain order, sort
your data before you migrate with an aggregation pipeline.

For more information on additional considerations for migrating your data, see `timeseries-best-practices`.

## Next Steps

If your original collection had secondary indexes, manually recreate them now.

If your time series collection includes `timeField` values before `1970-01-01T00:00:00.000Z` or after `2038-01-19T03:14:07.000Z`, MongoDB logs a warning and disables some query optimizations that make use of the `internal clustered index <manual-timeseries-internal-index>`. To regain query performance and resolve the log warning, `create a secondary index <timeseries-add-secondary-index>` on the `timeField`.

> **Seealso:** `timeseries-add-secondary-index`
