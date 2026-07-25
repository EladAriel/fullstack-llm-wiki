---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/find-projection-arg-option-diff.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can specify projection in two ways for :method:`~db.collection.find()` and :method:`~db.collection.findOne()`:

- Setting the `projection` parameter
- Setting the `options` parameter to `projection`
If you specify both parameters, the `projection` parameter takes precedence. To use `options.projection`, set the `projection` parameter to `null` or `undefined`.
