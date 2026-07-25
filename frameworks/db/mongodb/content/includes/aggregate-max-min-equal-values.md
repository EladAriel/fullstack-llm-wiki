---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregate-max-min-equal-values.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If multiple values compare as equal, |operatorName| may return any of those values. There is no guarantee which equal value |operatorName| returns.

For example, under a case-insensitive collation, `"a"` and `"A"` can compare as equal. There is no guarantee which will be returned.
