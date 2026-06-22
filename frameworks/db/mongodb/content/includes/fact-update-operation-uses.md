---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-update-operation-uses.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The update operation:

- uses the :update:`$set` operator to update the value of the
`size.uom` field to `"cm"` and the value of the `status` field to `"P"`,

- uses the :update:`$currentDate` operator to update the value
of the `lastModified` field to the current date. If `lastModified` field does not exist, :update:`$currentDate` will create the field. See :update:`$currentDate` for details.
