---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/find-projection-arg-option-diff.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You can specify projection in two ways for :method:`~db.collection.find()` and :method:`~db.collection.findOne()`:

- Setting the `projection` parameter
- Setting the `options` parameter to `projection`
If you specify both parameters, the `projection` parameter takes precedence. To use `options.projection`, set the `projection` parameter to `null` or `undefined`.
