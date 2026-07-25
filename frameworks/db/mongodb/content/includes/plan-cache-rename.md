---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/plan-cache-rename.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.0, the existing `queryHash` field is duplicated in a new field named `planCacheShapeHash`. If you're using an earlier MongoDB version, you'll only see the `queryHash` field. Future MongoDB versions will remove the deprecated `queryHash` field, and you'll need to use the `planCacheShapeHash` field instead.
