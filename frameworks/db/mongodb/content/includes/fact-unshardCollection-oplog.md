---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-unshardCollection-oplog.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** Unsharding a collection is a write-intensive operation that can result in an
increased `oplog` growth rate. To help mitigate this, consider the following
configuration changes:
- To prevent unbounded oplog growth, set a fixed oplog size.
- To reduce the chance of secondaries becoming stale, increase the oplog size.
For more details, see the `replica-set-oplog`.
