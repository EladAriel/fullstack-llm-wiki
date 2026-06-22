---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/write-concern-majority-and-transactions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you specify a :writeconcern:`"majority"` write concern for writes and the operation does not replicate to the  `calculated majority<calculating-majority-count>` of `replica set` members before it returns a response, then the data eventually replicates or rolls back. See `wc-wtimeout`.
