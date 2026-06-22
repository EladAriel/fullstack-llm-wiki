---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/backup-sharded-clusters.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# Backup and Restore a Self-Managed Sharded Cluster

The following tutorials describe backup and restoration for sharded clusters:

> **Tip:** .. include:: /includes/extracts/sharded-clusters-backup-restore-mongodump-mongorestore-restriction.rst

`/tutorial/backup-sharded-cluster-with-filesystem-snapshots` Use file system snapshots back up each component in the sharded cluster individually. The procedure involves stopping the cluster balancer. If your system configuration allows file system backups, this might be more efficient than using MongoDB tools.

`/tutorial/backup-sharded-cluster-with-database-dumps` Create backups using :binary:`~bin.mongodump` to back up each component in the cluster individually.

`/tutorial/schedule-backup-window-for-sharded-clusters` Limit the operation of the cluster balancer to provide a window for regular backup operations.

`/tutorial/restore-sharded-cluster` An outline of the procedure and consideration for restoring an entire sharded cluster from backup.

## Contents

- Use Snapshots </tutorial/backup-sharded-cluster-with-filesystem-snapshots>
- Use Database Dumps </tutorial/backup-sharded-cluster-with-database-dumps>
- Schedule Backups </tutorial/schedule-backup-window-for-sharded-clusters>
- Restore </tutorial/restore-sharded-cluster>
