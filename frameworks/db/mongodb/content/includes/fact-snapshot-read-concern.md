---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-snapshot-read-concern.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A query with read concern `"snapshot"` returns majority-committed data as it appears across shards from a specific single point in time in the recent past. Read concern `"snapshot"` provides its guarantees only if the transaction commits with write concern :writeconcern:`"majority"`.
