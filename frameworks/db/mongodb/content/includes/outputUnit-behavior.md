---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/outputUnit-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A `string` that specifies the time unit. Use one of these strings:

- `"week"`
- `"day"`
- `"hour"`
- `"minute"`
- `"second"`
- `"millisecond"`
If the `sortBy <setWindowFields-sortBy>` field is not a date, you must omit a `unit`. If you specify a `unit`, you must specify a date in the `sortBy <setWindowFields-sortBy>` field.
