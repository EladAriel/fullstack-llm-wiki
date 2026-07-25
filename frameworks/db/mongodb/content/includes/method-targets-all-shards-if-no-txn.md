---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/method-targets-all-shards-if-no-txn.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- If |method| is run outside a transaction, operations that target more
than one shard broadcast the operation to all shards in the cluster.

- If |method| is run inside a transaction, operations that target more
than one shard only target the relevant shards.
