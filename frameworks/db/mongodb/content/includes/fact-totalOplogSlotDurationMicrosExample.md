---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-totalOplogSlotDurationMicrosExample.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For example, consider the following writes with commit timestamps:

- writeA with Timestamp1
- writeB with Timestamp2
- writeC with Timestamp3
Suppose writeB commits first at Timestamp2. Replication is paused until writeA commits because writeA's oplog entry with Timestamp1 is required for replication to copy the oplog to secondary replica set members.
