---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/remainingOperationTimeEstimatedSecs-details.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`remainingOperationTimeEstimatedSecs`: estimated time remaining in seconds for the current `resharding operation <sharding-resharding>`. It is returned as `-1` when a new resharding operation starts.

Starting in MongoDB 7.0, `remainingOperationTimeEstimatedSecs` is also available on the coordinator during a resharding operation.

`remainingOperationTimeEstimatedSecs` is set to a pessimistic time estimate:

- The catch-up phase time estimate is set to the clone phase time, which
is a relatively long time.

- In practice, if there are only a few pending write operations, the
actual catch-up phase time is relatively short.
