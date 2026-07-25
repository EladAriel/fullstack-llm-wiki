---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-unshardCollection-oplog.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** Unsharding a collection is a write-intensive operation that can result in an
increased `oplog` growth rate. To help mitigate this, consider the following
configuration changes:
- To prevent unbounded oplog growth, set a fixed oplog size.
- To reduce the chance of secondaries becoming stale, increase the oplog size.
For more details, see the `replica-set-oplog`.
