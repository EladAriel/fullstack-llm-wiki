---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/resharding-mc-important.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Important:** These requirements are not enforced by the database. A failure to
allocate enough resources can result in:
- the database running out of space and shutting down
- decreased performance
- the operation taking longer than expected
If your application has time periods with less traffic, perform this
operation on the collection during that time if possible.
