---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-totalOplogSlotDurationMicrosExample.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For example, consider the following writes with commit timestamps:

- writeA with Timestamp1
- writeB with Timestamp2
- writeC with Timestamp3
Suppose writeB commits first at Timestamp2. Replication is paused until writeA commits because writeA's oplog entry with Timestamp1 is required for replication to copy the oplog to secondary replica set members.
