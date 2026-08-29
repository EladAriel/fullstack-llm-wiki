---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/backup-sharded-clusters.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.765223Z"
---
.. _backup-restore-sharded-clusters:

# Backup and Restore a Self-Managed Sharded Cluster

**meta:** :keywords: on-prem
   :description: Explore backup and restoration strategies for self-managed sharded clusters using mongodump, mongorestore, and file system snapshots to protect your data.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The following tutorials describe backup and restoration for sharded clusters:

**tip:** .. include:: /includes/extracts/sharded-clusters-backup-restore-mongodump-mongorestore-restriction.rst

:doc:`/tutorial/backup-sharded-cluster-with-filesystem-snapshots`
   Use file system snapshots back up each component in the sharded
   cluster individually. The procedure involves stopping the cluster
   balancer. If your system configuration allows file system backups,
   this might be more efficient than using MongoDB tools.

:doc:`/tutorial/backup-sharded-cluster-with-database-dumps`
   Create backups using :binary:`~bin.mongodump` to back up each
   component in the cluster individually.

:doc:`/tutorial/schedule-backup-window-for-sharded-clusters`
   Limit the operation of the cluster balancer to provide a window
   for regular backup operations.

:doc:`/tutorial/restore-sharded-cluster`
   An outline of the procedure and consideration for restoring an
   *entire* sharded cluster from backup.

:ref:`restore-sharded-dumps`
   Restore a sharded cluster from a backup created with
   :program:`mongodump`.


**toctree:** :titlesonly: 
   :hidden: 

   Use Snapshots </tutorial/backup-sharded-cluster-with-filesystem-snapshots>
   Use Database Dumps </tutorial/backup-sharded-cluster-with-database-dumps>
   Schedule Backups </tutorial/schedule-backup-window-for-sharded-clusters>
   Restore from File System Snapshots </tutorial/restore-sharded-cluster>
   Restore from Database Dumps </tutorial/restore-sharded-cluster-with-database-dumps>