---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/natural-sort-7.0-breaking-change.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Prior to MongoDB 7.0, :operator:`$natural` accepts incorrect type values, such as `0`, `NaN`, "X", and `-0.01`. After MongoDB 7.0, if you pass any value other than `1` and `-1` to :operator:`$natural`, MongoDB returns an error.
