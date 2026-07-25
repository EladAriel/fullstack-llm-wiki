---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bulkwrite-operation-batches.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The number of operations in each group cannot exceed the value of the :limit:`maxWriteBatchSize <Write Command Batch Limit Size>` of the database. The default value of `maxWriteBatchSize` is `100,000`. This value is shown in the `hello.maxWriteBatchSize` field.

This limit prevents issues with oversized error messages. If a group exceeds this :limit:`limit <Write Command Batch Limit Size>`, the client driver divides the group into smaller groups with counts less than or equal to the value of the limit. For example, with the `maxWriteBatchSize` value of `100,000`, if the queue consists of `200,000` operations, the driver creates 2 groups, each with `100,000` operations.

> **Note:** The driver only divides the group into smaller groups when using
the high-level API. If using :method:`db.runCommand()` directly
(for example, when writing a driver), MongoDB throws an error when
attempting to execute a write batch which exceeds the limit.

If the error report for a single batch grows too large, MongoDB truncates all remaining error messages to the empty string. If there are at least two error messages with total size greater than `1MB`, they are trucated.

The sizes and grouping mechanics are internal performance details and are subject to change in future versions.
