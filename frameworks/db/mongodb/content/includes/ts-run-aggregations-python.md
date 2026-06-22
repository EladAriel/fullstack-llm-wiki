---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-run-aggregations-python.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For additional query functionality, you can use the `aggregate()` method to run an `aggregation pipeline <aggregation-pipeline>`.

For more information on aggregations, see `manual-timeseries-aggregations-operators`.

This example:

- Finds all documents where the sensor ID is 5578
- Groups all documents by the date of the measurement
- Calculates the average of all temperature measurements that day
- Sorts the results by the average temperature in descending order
The example returns a `cursor <cursors>`. You can use the cursor to iterate through the resulting documents:

For more information on running aggregations using the PyMongo Driver, see :languages:`PyMongo Driver Aggregation </python/pymongo-driver/current/aggregation/>`.

For more information on how to access data from a cursor, see :languages:`Access Data From a Cursor </python/pymongo-driver/current/crud/query/cursors/>`.
