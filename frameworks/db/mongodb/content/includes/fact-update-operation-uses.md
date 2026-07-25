---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-update-operation-uses.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The update operation:

- uses the :update:`$set` operator to update the value of the
`size.uom` field to `"cm"` and the value of the `status` field to `"P"`,

- uses the :update:`$currentDate` operator to update the value
of the `lastModified` field to the current date. If `lastModified` field does not exist, :update:`$currentDate` will create the field. See :update:`$currentDate` for details.
