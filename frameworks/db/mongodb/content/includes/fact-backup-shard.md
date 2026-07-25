---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-backup-shard.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** Disabling the balancer is only necessary when **manually** taking backups,
either by calling :program:`mongodump` or scheduling a task that calls
`mongodump` at a specific time.
You do **not** have to disable the balancer when using coordinated backup
and restore processes:
- [MongoDB Atlas](https://www.mongodb.com/atlas/database)
- `MongoDB Cloud Manager
  <https://www.mongodb.com/cloud/cloud-manager>`_
- `MongoDB Ops Manager
  <https://www.mongodb.com/products/ops-manager>`_
