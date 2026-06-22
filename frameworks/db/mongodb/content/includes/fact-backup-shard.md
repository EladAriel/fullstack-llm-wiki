---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-backup-shard.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
