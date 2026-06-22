---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/restore-replica-set-from-backup.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# Restore a Self-Managed Replica Set from MongoDB Backups

This procedure outlines the process for taking MongoDB data and restoring that data into a new `replica set`. Use this approach for seeding test deployments from production backups or as part of disaster recovery.

> **Important:** You cannot restore a single data set to three new :binary:`~bin.mongod`
instances and **then** create a replica set. If you copy the data set
to each :binary:`~bin.mongod` instance and then create the replica set,
MongoDB will force the secondaries to perform an :term:`initial
sync`. The procedures in this document describe the correct and
efficient ways to deploy a restored replica set.

You can also use :binary:`~bin.mongorestore` to restore database files using data created with :binary:`~bin.mongodump`. See `/tutorial/backup-and-restore-tools` for more information.

## Considerations

.. include:: /includes/fact-stale-backup

## Restore Database into a Single Node Replica Set

.. include:: /includes/steps/restore-primary-from-backup.rst

.. include:: /includes/replacement-mms.rst

## Add Members to the Replica Set

MongoDB provides two options for restoring secondary members of a replica set:

- `Manually copy the database files <restore-rs-copy-db-files>`
to each data directory.

- `Allow initial sync <restore-rs-initial-sync>` to distribute
data automatically.

> **Note:** If your database is large, initial sync can take a long time to
complete. For large databases, it might be preferable to copy the
database files onto each host.

### Copy Database Files and Restart :binary:`~bin.mongod` Instance

Use the following sequence of operations to "seed" additional members of the replica set with the restored data by copying MongoDB data files directly.

.. include:: /includes/steps/restore-secondary-from-backup-directly.rst

### Update Secondaries using Initial Sync

Use the following sequence of operations to "seed" additional members of the replica set with the restored data using the default `initial sync <replica-set-initial-sync>` operation.

.. include:: /includes/steps/restore-secondary-from-backup-initial-sync.rst
