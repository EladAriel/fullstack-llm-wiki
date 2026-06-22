---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-migrate-with-tools.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================================

# Migrate Data into a Time Series Collection with Database Tools

Use the following steps to migrate data from an existing collection to a time series collection with :binary:`~bin.mongodump` and :binary:`~bin.mongorestore`.

## Steps

> **Seealso:** `timeseries-add-secondary-index`
If you insert a document into a collection with a `timeField`
value before `1970-01-01T00:00:00.000Z` or after
`2038-01-19T03:14:07.000Z`,
MongoDB logs a warning and prevents some query optimizations from
using the internal index. `Create a secondary index <timeseries-add-secondary-index>`
on the `timeField` to regain query performance and resolve the log
warning.
