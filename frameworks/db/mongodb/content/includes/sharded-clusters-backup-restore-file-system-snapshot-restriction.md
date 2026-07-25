---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharded-clusters-backup-restore-file-system-snapshot-restriction.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To take a backup with a file system snapshot, you must first stop the balancer, stop writes, and stop any schema transformation operations on the cluster.

MongoDB provides backup and restore operations that can run with the balancer and running transactions through the following services:

- [MongoDB Atlas](https://docs.atlas.mongodb.com/)
- [MongoDB Cloud Manager](https://docs.cloudmanager.mongodb.com/)
- [MongoDB Ops Manager](https://docs.opsmanager.mongodb.com/)
