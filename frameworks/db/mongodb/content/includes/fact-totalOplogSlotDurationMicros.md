---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-totalOplogSlotDurationMicros.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The `totalOplogSlotDurationMicros` in the slow query log message shows the time between a write operation getting a commit timestamp to commit the storage engine writes and actually committing. `mongod` supports parallel writes. However, it commits write operations with commit timestamps in any order.
