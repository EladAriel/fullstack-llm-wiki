---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/replication/fact-oplog-window-definition.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`oplog` entries are time-stamped. The oplog window is the time difference between the newest and the oldest timestamps in the `oplog`. If a secondary node loses connection with the primary, it can only use `replication <replication>` to sync up again if the connection is restored within the oplog window.
