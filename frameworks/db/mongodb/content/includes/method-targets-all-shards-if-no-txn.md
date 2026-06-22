---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/method-targets-all-shards-if-no-txn.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- If |method| is run outside a transaction, operations that target more
than one shard broadcast the operation to all shards in the cluster.

- If |method| is run inside a transaction, operations that target more
than one shard only target the relevant shards.
