---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/plan-cache-rename.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.0, the existing `queryHash` field is duplicated in a new field named `planCacheShapeHash`. If you're using an earlier MongoDB version, you'll only see the `queryHash` field. Future MongoDB versions will remove the deprecated `queryHash` field, and you'll need to use the `planCacheShapeHash` field instead.
