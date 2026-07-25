---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-snapshot-read-concern.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A query with read concern `"snapshot"` returns majority-committed data as it appears across shards from a specific single point in time in the recent past. Read concern `"snapshot"` provides its guarantees only if the transaction commits with write concern :writeconcern:`"majority"`.
