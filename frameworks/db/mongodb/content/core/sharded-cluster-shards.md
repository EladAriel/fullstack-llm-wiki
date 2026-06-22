---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/sharded-cluster-shards.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======

# Shards

A `shard` contains a subset of sharded data for a `sharded cluster`. Together, the cluster's shards hold the entire data set for the cluster.

Shards must be deployed as a `replica set` to provide redundancy and high availability.

> **Important:** Sharded clusters use the write concern `"majority"` for a lot of internal
operations. Using an arbiter in a sharded cluster is discouraged due to
`replica-set-arbiter-performance-psa`.

> **Warning:** **Typically, do not perform operations directly on a shard because
they might cause data corruption or data loss.** Users, clients, or
applications should only directly connect to a shard to perform local
administrative or maintenance operations.

Performing queries on a single shard only returns a subset of data. Connect to the :binary:`~bin.mongos` to perform cluster level operations, including read or write operations.

> **Important:** MongoDB does not guarantee that any two contiguous `chunks<chunk>`
reside on a single shard.

## Primary Shard

Each database in a sharded cluster has a primary shard. It is the default shard for all unsharded collections in the database. All unsharded collections for a database are created on the database primary shard by default. Starting in MongoDB 8.0, you can move unsharded collections to another shard using :dbcommand:`moveCollection`. The primary shard has no relation to the primary in a replica set.

The :binary:`~bin.mongos` selects the primary shard when creating a new database by picking the shard in the cluster that has the least amount of data. :binary:`~bin.mongos` uses the `totalSize` field returned by the :dbcommand:`listDatabases` command as a part of the selection criteria.

.. include:: /images/sharded-cluster-primary-shard.rst

To change the primary shard for a database, use the :dbcommand:`movePrimary` command. The process of migrating the primary shard may take significant time to complete, and you should not access the collections associated to the database until it completes. Depending on the amount of data being migrated, the migration may affect overall cluster operations. Consider the impact to cluster operations and network load before attempting to change the primary shard.

When you deploy a new `sharded cluster` with shards that were previously used as replica sets, all existing databases continue to reside on their original replica sets. Databases created subsequently may reside on any shard in the cluster.

## Shard Status

Use the :method:`sh.status()` method in :binary:`~bin.mongosh` to see an overview of the cluster. This reports includes which shard is primary for the database and the `chunk` distribution across the shards. See :method:`sh.status()` method for more details.

## Sharded Cluster Security

Use `/core/security-internal-authentication` to enforce intra-cluster security and prevent unauthorized cluster components from accessing the cluster. You must start each :binary:`~bin.mongod` in the cluster with the appropriate security settings in order to enforce internal authentication.

.. include:: /includes/intra-cluster-authentication.rst

See `/tutorial/deploy-sharded-cluster-with-keyfile-access-control` for a tutorial on deploying a secured sharded cluster.

### Shard Local Users

Each shard supports `/core/authorization` (RBAC) for restricting unauthorized access to shard data and operations. Start each :binary:`~bin.mongod` in the replica set with the :option:`--auth <mongod --auth>` option to enforce RBAC. Alternatively, enforcing `/core/security-internal-authentication` for intra-cluster security also enables user access controls via RBAC.

.. include:: /includes/intra-cluster-authentication.rst

Each shard has its own shard-local users. These users cannot be used on other shards, nor can they be used for connecting to the cluster via a :binary:`~bin.mongos`.

See `/tutorial/enable-authentication` for a tutorial on enabling adding users to an RBAC-enabled MongoDB deployment.
