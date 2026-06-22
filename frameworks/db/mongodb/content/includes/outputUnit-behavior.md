---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/outputUnit-behavior.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A `string` that specifies the time unit. Use one of these strings:

- `"week"`
- `"day"`
- `"hour"`
- `"minute"`
- `"second"`
- `"millisecond"`
If the `sortBy <setWindowFields-sortBy>` field is not a date, you must omit a `unit`. If you specify a `unit`, you must specify a date in the `sortBy <setWindowFields-sortBy>` field.
