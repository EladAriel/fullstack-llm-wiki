---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-run-aggregations-mongosh.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For additional query functionality, you can use the :method:`db.collection.aggregate()` method to run an `aggregation pipeline <aggregation-pipeline>`.

For more information on aggregations, see `manual-timeseries-aggregations-operators`.

This example:

- Groups all documents by the date of the measurement
- Calculates the average of all temperature measurements that day
- Returns a `cursor <cursors>` that can be used to iterate through the
resulting documents

For more information on how to access data from a cursor, see:

- `Iterate a Cursor in mongosh <read-operations-cursors>`
- `<doc-cursor-methods>`
