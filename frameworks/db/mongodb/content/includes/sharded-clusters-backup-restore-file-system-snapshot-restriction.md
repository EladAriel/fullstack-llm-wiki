---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sharded-clusters-backup-restore-file-system-snapshot-restriction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To take a backup with a file system snapshot, you must first stop the balancer, stop writes, and stop any schema transformation operations on the cluster.

MongoDB provides backup and restore operations that can run with the balancer and running transactions through the following services:

- [MongoDB Atlas](https://docs.atlas.mongodb.com/)
- [MongoDB Cloud Manager](https://docs.cloudmanager.mongodb.com/)
- [MongoDB Ops Manager](https://docs.opsmanager.mongodb.com/)
