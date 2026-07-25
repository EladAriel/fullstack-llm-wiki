---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/5.0-changes/fact-getLastError-alternatives.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Any code explicitly using `getLastError`,  `db.getLastError()`, or `db.getLastErrorObj()` should instead use the CRUD API to issue the write with the desired `write concern <write-concern>`. Information about the success or failure of the write operation will be provided directly by the driver as a return value.
