---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/query-shape-hash-string.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A query shape hash is a string that uniquely identifies the query shape. An example query shape hash is `"F42757F1AEB68B4C5A6DE6182B29B01947C829C926BCC01226BDA4DDE799766C"`.

To obtain the query shape hash string, do any of these:

- Use a :pipeline:`$querySettings` stage in an :ref:`aggregation
pipeline <aggregation-pipeline>` and examine the `queryShapeHash` field.

- Examine the `database profiler <database-profiling>` output.
- View the `slow query logs <log-message-slow-ops>`.
If you set the query settings using a hash string, then you won't have the `representativeQuery` field in the `$querySettings` aggregation stage output.
