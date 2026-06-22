---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/w-1-rollback-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** If write operations use :writeconcern:`{ w: 1 } <\<number\>>` write concern,
the rollback directory may exclude writes submitted after an
`oplog hole` if the primary restarts before the write operation
completes.
