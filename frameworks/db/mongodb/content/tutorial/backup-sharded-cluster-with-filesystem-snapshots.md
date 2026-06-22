---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/backup-sharded-cluster-with-filesystem-snapshots.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================================

# Back Up a Sharded Cluster with File System Snapshots

## Overview

This document describes a procedure for taking a backup of all components of a self-managed `sharded cluster`. This procedure uses file system snapshots to capture a copy of the :binary:`~bin.mongod` instance.

.. include:: /includes/note-shard-cluster-backup.rst

For more information on backups in MongoDB and backups of sharded clusters in particular, see `/core/backups` and `/administration/backup-sharded-clusters`.

## Considerations

### Transactions Across Shards

.. include:: /includes/sharded-clusters-backup-restore-file-system-snapshot-restriction.rst

### Encrypted Storage Engine (MongoDB Enterprise Only)

.. include:: /includes/fact-aes256-backups.rst

### Balancer

It is essential that you stop the `balancer <sharding-internals-balancing>` before capturing a backup.

If the balancer is active while you capture backups, the backup artifacts may be incomplete or have duplicate data, as `chunks <chunk>` may migrate while recording backups.

### Precision

In this procedure, you will stop the cluster balancer and take a backup up of the `config database`, and then take backups of each shard in the cluster using a file-system snapshot tool. If you need an exact moment-in-time snapshot of the system, you will need to stop all writes before taking the file system snapshots; otherwise the snapshot will only approximate a moment in time.

### Consistency

To back up a sharded cluster, you must use the :dbcommand:`fsync` command or :method:`db.fsyncLock` method to stop writes on the cluster. This helps reduce the likelihood of inconsistencies in the backup.

> **Note:** These steps can only produce a consistent backup if they are
followed exactly and no operations are in progress when you
begin.

.. include:: /includes/fact-backup-snapshots-with-ebs-in-raid10.rst

### Version Compatibility

This procedure requires a version of MongoDB that supports fsync locking from :program:`mongos`.

:dbcommand:`fsyncUnlock` commands

.. include:: /includes/fsync-mongos

### Stale Data

.. include:: /includes/fact-stale-backup

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Steps

To take a self-managed backup of a sharded cluster, complete the following steps:
