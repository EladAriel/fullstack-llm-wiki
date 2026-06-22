---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/highwatermark-tip-idle-shards.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The server periodically advances the timestamp in highwatermark resume tokens. On idle shards with infrequent writes, this advancement might not occur frequently enough for some use cases. To advance the highwatermark timestamp more frequently, you can write no-op entries to the oplog on idle shards using the :dbcommand:`appendOplogNote` command.
