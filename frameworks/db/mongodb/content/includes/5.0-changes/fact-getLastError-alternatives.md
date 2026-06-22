---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/5.0-changes/fact-getLastError-alternatives.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Any code explicitly using `getLastError`,  `db.getLastError()`, or `db.getLastErrorObj()` should instead use the CRUD API to issue the write with the desired `write concern <write-concern>`. Information about the success or failure of the write operation will be provided directly by the driver as a return value.
