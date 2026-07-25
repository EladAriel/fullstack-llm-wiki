---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-totalOplogSlotDurationMicros.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The `totalOplogSlotDurationMicros` in the slow query log message shows the time between a write operation getting a commit timestamp to commit the storage engine writes and actually committing. `mongod` supports parallel writes. However, it commits write operations with commit timestamps in any order.
