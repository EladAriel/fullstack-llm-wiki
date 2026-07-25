---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/highwatermark-tip-idle-shards.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The server periodically advances the timestamp in highwatermark resume tokens. On idle shards with infrequent writes, this advancement might not occur frequently enough for some use cases. To advance the highwatermark timestamp more frequently, you can write no-op entries to the oplog on idle shards using the :dbcommand:`appendOplogNote` command.
