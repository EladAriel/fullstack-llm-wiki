---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/migrate-sharded-cluster-to-new-hardware.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================================

# Migrate a Self-Managed Sharded Cluster to Different Hardware

The tutorial is specific to MongoDB {+latest-lts-version+}. For earlier versions of MongoDB, refer to the corresponding version of the MongoDB Manual.

.. include:: /includes/fact-mirrored-config-servers-deprecated.rst

This procedure moves the components of the `sharded cluster` to a new hardware system without downtime for reads and writes.

> **Important:** any operation that modifies the cluster metadata in any way. For
example, do not create or drop databases, create or drop collections,
or use any sharding commands.

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Disable the Balancer

Disable the balancer to stop `chunk migration <sharding-balancing>` and do not perform any metadata write operations until the process finishes. If a migration is in progress, the balancer will complete the in-progress migration before stopping.

To disable the balancer, connect to one of the cluster's :binary:`~bin.mongos` instances and issue the following method: [#autosplit-stop]_

```javascript
sh.stopBalancer()
```

To check the balancer state, issue the :method:`sh.getBalancerState()` method.

For more information, see `sharding-balancing-disable-temporarily`.

.. include:: /includes/extracts/4.2-changes-stop-balancer-autosplit.rst

## Migrate Each Config Server Separately

.. include:: /includes/fact-csrs-versionchanged.rst

.. include:: /includes/fact-config-server-replica-set-restrictions.rst

For each member of the config server replica set:

> **Important:**

.. include:: /includes/steps/replace-disabled-config-server.rst

## Restart the `mongos` Instances

With replica set config servers, the :binary:`~bin.mongos` instances specify in the :option:`--configdb <mongos --configdb>` or :setting:`sharding.configDB` setting the config server replica set name and at least one of the replica set members. The :binary:`~bin.mongos` instances for the sharded cluster must specify the same config server replica set name but can specify different members of the replica set.

If a :binary:`~bin.mongos` instance specifies a migrated replica set member in the :option:`--configdb <mongos --configdb>` or :setting:`sharding.configDB` setting, update the config server setting for the next time you restart the :binary:`~bin.mongos` instance.

For more information, see `sharding-setup-start-mongos`.

## Migrate the Shards

Migrate the shards one at a time. For each shard, follow the appropriate procedure in this section.

### Migrate a Replica Set Shard

To migrate a sharded cluster, migrate each member separately. First migrate the non-primary members, and then migrate the `primary` last.

If the replica set has two voting members, add an `arbiter </core/replica-set-arbiter>` to the replica set to ensure the set keeps a majority of its votes available during the migration. You can remove the arbiter after completing the migration.

Migrate a Member of a Replica Set Shard ````````````````````````````````````````

1. Shut down the :binary:`~bin.mongod` process. To ensure a
clean shutdown, use the :dbcommand:`shutdown` command.

#. Move the data directory (i.e., the :setting:`~storage.dbPath`) to the new machine.

#. Restart the :binary:`~bin.mongod` process at the new location.

#. Connect to the replica set's current primary.

#. If the hostname of the member has changed, use :method:`rs.reconfig()` to update the `replica set configuration document </reference/replica-configuration>` with the new hostname.

For example, the following sequence of commands updates the hostname for the instance at position `2` in the `members` array:

```javascript
   cfg = rs.conf()
   cfg.members[2].host = "pocatello.example.net:27018"
   rs.reconfig(cfg)

For more information on updating the configuration document, see
:ref:`replica-set-reconfiguration-usage`.
```

#. To confirm the new configuration, issue :method:`rs.conf()`.

#. Wait for the member to recover. To check the member's state, issue :method:`rs.status()`.

Migrate the Primary in a Replica Set Shard ``````````````````````````````````````````

While migrating the replica set's primary, the set must elect a new primary. This failover process which renders the replica set unavailable to perform reads or accept writes for the duration of the election, which typically completes quickly. If possible, plan the migration during a maintenance window.

1. Step down the primary to allow the normal :ref:`failover
<replica-set-failover>` process.  To step down the primary, connect to the primary and issue the either the :dbcommand:`replSetStepDown` command or the :method:`rs.stepDown()` method. The following example shows the :method:`rs.stepDown()` method:

```javascript
   rs.stepDown()
```

#. Once the primary has stepped down and another member has become :replstate:`PRIMARY` state. To migrate the stepped-down primary, follow the `migrate-replica-set-shard-member` procedure

You can check the output of :method:`rs.status()` to confirm the change in status.

## Re-Enable the Balancer

To complete the migration, re-enable the balancer to resume `chunk migrations <sharding-balancing>`.

Connect to one of the cluster's :binary:`~bin.mongos` instances and pass `true` to the :method:`sh.startBalancer()` method: [#autosplit-start]_

```javascript
sh.startBalancer()
```

To check the balancer state, issue the :method:`sh.getBalancerState()` method.

For more information, see `sharding-balancing-enable`.

.. include:: /includes/extracts/4.2-changes-start-balancer-autosplit.rst
