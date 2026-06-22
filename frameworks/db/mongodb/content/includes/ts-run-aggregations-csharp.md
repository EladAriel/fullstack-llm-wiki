---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-run-aggregations-csharp.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For additional query functionality, you can use the `Aggregate()` method to run an `aggregation pipeline <aggregation-pipeline>`.

For more information on aggregations, see `manual-timeseries-aggregations-operators`.

This example creates an aggregation pipeline that:

- Matches all documents with a `sensor.sensor_id` of "5578"
- Groups those documents by the date of the measurement
- Calculates the average of all temperature measurements that day in a new property
called `avgTemp`

- Returns a `List<BsonDocument>`
For more information on running aggregations using the C# Driver, see :driver:`C# Driver Aggregations </csharp/sync/current/aggregation/>`.

For more information on how to access data from a cursor, see :driver:`Access Data From a Cursor </csharp/sync/current/crud/query-documents/cursor/>`.
