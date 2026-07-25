---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/database-profiler-levels.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

`0` The profiler is off and does not collect any data. This is the default profiler level.

`1` The profiler collects data for operations that exceed the `slowms` threshold or match a specified `filter <set-profiling-level-options-filter>`.

When a filter is set:

- The `slowms` and `sampleRate` options are not used for
profiling.

- The profiler only captures operations that match the
`filter <set-profiling-level-options-filter>`.

`2` The profiler collects data for all operations.

When set to level `2`, the profiler ignores user provided values for `slowms` and `filter`.
