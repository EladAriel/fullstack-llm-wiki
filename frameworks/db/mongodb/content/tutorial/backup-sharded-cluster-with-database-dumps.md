---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/backup-sharded-cluster-with-database-dumps.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================================

# Back Up a Self-Managed Sharded Cluster with a Database Dump

Starting in MongoDB 7.1 (also available starting in 7.0.2, 6.0.11, and 5.0.22), you can back up data on sharded clusters using :program:`mongodump`.

## About this Task

:program:`mongodump` is a utility that creates a binary export of database content. You can use the `mongodump` utility to take self-managed backups of a sharded cluster.

To back up a sharded cluster with `mongodump`, you must stop the balancer, stop writes, and stop any schema transformation operations on the cluster. This helps reduce the likelihood of inconsistencies in the backup.

MongoDB provides backup and restore operations that can run with the balancer and running transactions through the following services:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)
- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager)
- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager)
### Stale Backups

.. include:: /includes/fact-stale-backup

## Before you Begin

This task uses :program:`mongodump` to back up a sharded cluster. Ensure that you have a cluster running that contains data in sharded collections.

### Version Compatibility

This procedure requires a version of MongoDB that supports fsync locking from :program:`mongos`.

:dbcommand:`fsyncUnlock` commands

.. include:: /includes/fsync-mongos

### Admin Privileges

To use this procedure, your MongoDB user must have the :authaction:`fsync` authorization, which can be available through a custom role or using the built-in :authrole:`hostManager` role.

With this authorization you can run the :dbcommand:`fsync` and :dbcommand:`fsyncUnlock` commands.

## Steps

To take a self-managed backup of a sharded cluster, complete the following steps:

## Next Steps

You can restore data from a :program:`mongodump` backup using :program:`mongorestore`.

- To migrate to a replica set or standalone server, execute `mongorestore`
against :program:`mongod`.

- To restore to a sharded cluster, execute `mongorestore` against
:program:`mongos` with :option:`--nsExclude <mongorestore --nsExclude>` set to exclude the `config` database:

```sh
  mongorestore --nsExclude='config.*' /data/backup 
```

> **Important:** `mongorestore` does not shard restored collections on the destination cluster.
To ensure that a restored collection is sharded on the destination cluster,
create a collection with the same namespace on the destination cluster then
`shard the collection <sharding-shard-key-creation>` before running `mongorestore`.
The `balancer <sharding-balancing>` will eventually spread the restored documents
across the shards of the destination cluster.

For more information, see `manual-tutorial-backup-and-restore`.
