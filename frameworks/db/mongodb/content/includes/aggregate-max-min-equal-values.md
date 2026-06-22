---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregate-max-min-equal-values.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If multiple values compare as equal, |operatorName| may return any of those values. There is no guarantee which equal value |operatorName| returns.

For example, under a case-insensitive collation, `"a"` and `"A"` can compare as equal. There is no guarantee which will be returned.
