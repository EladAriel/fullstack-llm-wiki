---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/write-concern-majority-and-transactions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you specify a :writeconcern:`"majority"` write concern for writes and the operation does not replicate to the  `calculated majority<calculating-majority-count>` of `replica set` members before it returns a response, then the data eventually replicates or rolls back. See `wc-wtimeout`.
