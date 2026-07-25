---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/remainingOperationTimeEstimatedSecs-details.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

`remainingOperationTimeEstimatedSecs`: estimated time remaining in seconds for the current `resharding operation <sharding-resharding>`. It is returned as `-1` when a new resharding operation starts.

Starting in MongoDB 7.0, `remainingOperationTimeEstimatedSecs` is also available on the coordinator during a resharding operation.

`remainingOperationTimeEstimatedSecs` is set to a pessimistic time estimate:

- The catch-up phase time estimate is set to the clone phase time, which
is a relatively long time.

- In practice, if there are only a few pending write operations, the
actual catch-up phase time is relatively short.
