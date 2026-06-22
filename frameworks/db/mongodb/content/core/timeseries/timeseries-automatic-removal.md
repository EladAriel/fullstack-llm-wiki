---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-automatic-removal.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================================

# Set up Automatic Removal for Time Series Collections (TTL)

## Behavior

### Timing of Delete Operations

MongoDB doesn't guarantee that expired data will be deleted immediately upon expiration. Once all documents in a bucket are expired, the background task that removes expired buckets removes the bucket during the next run. The maximum span of time that a single bucket is allowed to cover is controlled by the `granularity` of the time series collection:

The background task that removes expired buckets runs every 60 seconds. Therefore, documents may remain in a collection during the period between the expiration of the document, the expiration of all other documents in the bucket and the running of the background task.

Because the duration of the removal operation depends on the workload of your mongod instance, expired data may exist for some time beyond the 60 second period between runs of the background task.
