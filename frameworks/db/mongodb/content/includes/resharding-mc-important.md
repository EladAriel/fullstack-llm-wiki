---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/resharding-mc-important.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** These requirements are not enforced by the database. A failure to
allocate enough resources can result in:
- the database running out of space and shutting down
- decreased performance
- the operation taking longer than expected
If your application has time periods with less traffic, perform this
operation on the collection during that time if possible.
