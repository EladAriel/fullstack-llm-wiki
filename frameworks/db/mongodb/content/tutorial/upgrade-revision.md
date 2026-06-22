---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/upgrade-revision.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================================

# Upgrade to the Latest Self-Managed Patch Release of MongoDB

MongoDB version numbers have the form `X.Y.Z` where `Z` refers to the patch release number. Patch releases provide security patches, bug fixes, and new or changed features that generally do not contain any backward breaking changes. Always upgrade to the latest patch release in your release series.

For more information on versioning, including Atlas major and minor upgrades, see `MongoDB Versioning <release-version-numbers>`.

## About this Task

This page describes upgrade procedures for the MongoDB {+latest-lts-version+} release series. To upgrade a different release series, refer to the corresponding version of the manual.

## Before You Begin

Review the following sections to ensure that your deployment is ready to be upgraded.

### Backup

Ensure you have an up-to-date backup of your data set. See `backup-methods`.

### Compatibility Considerations

Consult the following documents for any special considerations or compatibility issues specific to your MongoDB release:

- `Release notes <server-release-notes-landing>`
- :driver:`Driver documentation </>`
### Maintenance Window

If your installation includes `replica sets <replica set>`, set the upgrade to occur during a predefined maintenance window.

### Staging Environment Check

Before you upgrade a production environment, use the procedures in this document to upgrade a staging environment that reproduces your production environment. Ensure that your production configuration is compatible with all changes before upgrading.

## Steps

Upgrade each :binary:`~bin.mongod` and :binary:`~bin.mongos` binary separately. Follow this upgrade procedure:

#. For deployments that use authentication, first upgrade all of your MongoDB Drivers. To upgrade, see the :driver:`documentation for your driver </>`.

#. Upgrade any standalone instances. See `upgrade-mongodb-instance`.

#. Upgrade any replica sets that are not part of a sharded cluster, as described in `upgrade-replica-set`.

#. Upgrade sharded clusters, as described in `upgrade-sharded-cluster`.

### Check Feature Compatibility Version (FCV)

Before upgrading the binaries, confirm that the `featureCompatibilityVersion` has been fully upgraded on all relevant components of your deployment. If the prior FCV upgrade did not complete successfully, restarting the binary with a higher version can cause the node to crash.

For `Replica Sets <upgrade-replica-set>`:

To verify the FCV, connect to each member of the replica set and run the following command:

```javascript
db.adminCommand( { getParameter: 1, featureCompatibilityVersion: 1 } )
```

All members should return a result that includes the following:

```javascript
"featureCompatibilityVersion" : { "version" : "{+latest-lts-version+}" }
```

For `Sharded Clusters <upgrade-sharded-cluster>`:

Perform the same check on all config servers and shards:

- For shards that are replica sets, verify FCV on each member of the replica set.
- For standalone shard instances, run the command directly on the instance.
Wait for all members to report the required FCV before proceeding with the binary upgrade.

### Upgrade a MongoDB Instance

To upgrade a {+latest-lts-version+} :binary:`~bin.mongod` or :binary:`~bin.mongos` instance, use one of these approaches:

- Upgrade the instance using the operating system's package management
tool and the official MongoDB packages. This is the preferred approach. See `/installation`.

- Upgrade the instance by replacing the existing binaries with new
binaries. See `upgrade-replace-binaries`.

Replace the Existing Binaries `````````````````````````````

This section describes how to upgrade MongoDB by replacing the existing binaries. The preferred approach to an upgrade is to use the operating system's package management tool and the official MongoDB packages, as described in `/installation`.

To upgrade a :binary:`~bin.mongod` or :binary:`~bin.mongos` instance by replacing the existing binaries:

1. Download the binaries for the latest MongoDB patch release from the
MongoDB Download Page and store the binaries in a temporary location. The binaries download as compressed files that uncompress to the directory structure used by the MongoDB installation.

#. Shutdown the instance.

#. Replace the existing MongoDB binaries with the downloaded binaries.

#. Make any required configuration file changes.

#. Restart the instance.

### Upgrade Replica Sets

To upgrade a {+latest-lts-version+} replica set, upgrade each member individually, starting with the `secondaries <secondary>` and finishing with the `primary`. Plan the upgrade during a predefined maintenance window.

.. include:: /includes/upgrade-downgrade-replica-set.rst

Upgrade Secondaries ```````````````````

Upgrade each secondary separately as follows:

1. Upgrade the secondary's :binary:`~bin.mongod` binary by following the
instructions in `upgrade-mongodb-instance`.

#. After upgrading a secondary, wait for the secondary to recover to the `SECONDARY` state before upgrading the next instance. To check the member's state, issue :method:`rs.status()` in :binary:`~bin.mongosh`.

The secondary may briefly go into `STARTUP2` or `RECOVERING`. This is normal. Make sure to wait for the secondary to fully recover to `SECONDARY` before you continue the upgrade.

Upgrade the Primary ```````````````````

1. Step down the primary to initiate the normal :ref:`failover
<replica-set-failover>` procedure. Using one of the following:

- The :method:`rs.stepDown()` helper in :binary:`~bin.mongosh`.
- The :dbcommand:`replSetStepDown` database command.
During failover, the set cannot accept writes. Typically this takes 10-20 seconds. Plan the upgrade during a predefined maintenance window.

> **Note:**    shutting down the primary. Stepping down expedites the
   failover procedure.

#. Once the primary has stepped down, call the :method:`rs.status()` method from :binary:`~bin.mongosh` until you see that another member has assumed the `PRIMARY` state.

#. Shut down the original primary and upgrade its instance by following the instructions in `upgrade-mongodb-instance`.

### Upgrade Sharded Clusters

To upgrade a {+latest-lts-version+} sharded cluster:

1. Disable the cluster's balancer as described in
`sharding-balancing-disable-temporarily`.

#. Upgrade the `config servers <sharding-config-server>`.

To upgrade the config server replica set, use the procedures in `upgrade-replica-set`.

#. Upgrade each shard.

- If a shard is a replica set, upgrade the shard using the
procedure titled `upgrade-replica-set`.

- If a shard is a standalone instance, upgrade the shard using the
procedure titled `upgrade-mongodb-instance`.

#. Once the config servers and the shards have been upgraded, upgrade each :binary:`~bin.mongos` instance by following the instructions in `upgrade-mongodb-instance`. You can upgrade the :binary:`~bin.mongos` instances in any order.

#. Re-enable the balancer, as described in `sharding-balancing-re-enable`.

## Learn More

- `production-notes`
- `sharding-manage-shards`
- `replica-set-sync`
