---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/restart-sharded-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Restart a Self-Managed Sharded Cluster

The tutorial is specific to MongoDB {+latest-lts-version+}. For earlier versions of MongoDB, refer to the corresponding version of the MongoDB Manual.

This procedure demonstrates the shutdown and startup sequence for restarting a sharded cluster. Stopping or starting the components of a sharded cluster in a different order may cause communication errors between members. For example, `shard <shards-concepts>` servers may appear to hang if there are no `config servers <sharding-config-server>` available.

> **Important:** maintenance period. During this period, applications should stop
all reads and writes to the cluster in order to prevent potential
data loss or reading stale data.

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Disable the Balancer

Disable the balancer to stop `chunk migration <sharding-balancing>` and do not perform any metadata write operations until the process finishes. If a migration is in progress, the balancer will complete the in-progress migration before stopping.

To disable the balancer, connect to one of the cluster's :binary:`~bin.mongos` instances and issue the following command: [#autosplit-stop]_

```javascript
sh.stopBalancer()
```

To check the balancer state, issue the :method:`sh.getBalancerState()` command.

For more information, see `sharding-balancing-disable-temporarily`.

.. include:: /includes/extracts/4.2-changes-stop-balancer-autosplit.rst

## Stop Sharded Cluster

.. include:: /includes/steps/stop-sharded-cluster.rst

## Start Sharded Cluster

.. include:: /includes/steps/start-sharded-cluster.rst

## Re-Enable the Balancer

Re-enable the balancer to resume `chunk migrations <sharding-balancing>`.

Connect to one of the cluster's :binary:`~bin.mongos` instances and run the :method:`sh.startBalancer()` command: [#autosplit-start]_

```javascript
sh.startBalancer()
```

To check the balancer state, issue the :method:`sh.getBalancerState()` command.

For more information, see `sharding-balancing-enable`.

.. include:: /includes/extracts/4.2-changes-start-balancer-autosplit.rst

## Validate Cluster Accessibility

Connect a :binary:`mongo <bin.mongo>` shell to one of the cluster's :binary:`mongos <bin.mongos>` processes. Use :method:`sh.status()` to check the overall cluster status.

To confirm that all shards are accessible and communicating, insert test data into a temporary sharded collection. Confirm that data is being split and migrated between each shard in your cluster. You can connect a :binary:`mongo <bin.mongo>` shell to each shard primary and use :method:`db.collection.find()` to validate that the data was sharded as expected.

> **Important:** do not start application reads and writes to the cluster
until after confirming the cluster is healthy and accessible.
