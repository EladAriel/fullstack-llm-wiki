---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/manage-sharded-cluster-balancer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Manage Sharded Cluster Balancer

This page describes common administrative procedures related to balancing. For an introduction to balancing, see `sharding-balancing`. For lower level information on balancing, see `sharding-balancing-internals`.

The balancer process has moved from the :binary:`~bin.mongos` instances to the primary member of the config server replica set.

## Check the Balancer State

:method:`sh.getBalancerState()` checks if the balancer is enabled (i.e. that the balancer is permitted to run). :method:`sh.getBalancerState()` does not check if the balancer is actively migrating data.

To see if the balancer is enabled in your `sharded cluster`, run the following command, which returns a boolean:

```javascript
sh.getBalancerState()
```

You can also see if the balancer is enabled using :method:`sh.status()`. The `sh.status.balancer.currently-enabled` field indicates whether the balancer is enabled, and the `sh.status.balancer.currently-running` field indicates if the balancer is currently running.

## Check if Balancer is Running

To see if the balancer process is active in your `cluster <sharded cluster>`:

#. Connect to any :binary:`~bin.mongos` in the cluster using the :binary:`~bin.mongosh` shell.

#. Use the following operation to determine if the balancer is running:

```javascript
   sh.isBalancerRunning()
```

## Configure Default Range Size

The default range size for a sharded cluster is 128 megabytes. In most situations, the default size is appropriate for splitting and migrating chunks. For information on how range size affects deployments, see details, see `sharding-range-size`.

Changing the default range size affects ranges that are processes during migrations and auto-splits but does not retroactively affect all ranges.

To configure default range size, see `tutorial-modifying-chunk-size`.

## Schedule the Balancing Window

In some situations, particularly when your data set grows slowly and a migration can impact performance, it is useful to ensure that the balancer is active only at certain times. By default, the balancer process is always enabled and migrating chunks. The following procedure specifies the `activeWindow`, which is the timeframe during which the `balancer` is able to migrate chunks:

.. include:: /includes/steps/schedule-balancer-window.rst

## Check Balancing Window

To see the current balancing window, run the following command:

```javascript
use config
db.settings.find( { _id: "balancer" } )
```

## Remove a Balancing Window Schedule

If you have `set the balancing window <sharding-schedule-balancing-window>` and wish to remove the schedule so that the balancer is always running, use :update:`$unset` to clear the schedule.

Clear the `activeWindow` by running:

Clear the `activeWindowDOW` by running:

If you have both `activeWindow` and `activeWindowDOW` set, you must individually unset both using :update:`$unset` as shown above.

## Disable the Balancer

> **Important:** .. include:: /includes/sharding/disable-balancer-warning.rst

By default, the balancer may run at any time and only moves chunks as needed. To disable the balancer for a short period of time and prevent all migration, use the following procedure:

#. Connect to any :binary:`~bin.mongos` in the cluster using the :binary:`~bin.mongosh` shell.

#. Issue the following operation to disable the balancer:

```javascript
   sh.stopBalancer()

If a migration is in progress, the system will complete the
in-progress migration before stopping.
```

#. To verify that the balancer won't start, run the following command, which returns `false` if the balancer is disabled:

```javascript
   sh.getBalancerState()

Optionally, to verify no migrations are in progress after disabling,
run the following operation in the :binary:`~bin.mongosh` shell:

.. code-block:: javascript

   use config
   while( sh.isBalancerRunning() ) {
             print("waiting...");
             sleep(1000);
   }
```

> **Note:** To disable the balancer from a driver,
use the :command:`balancerStop` command against the `admin` database,
as in the following:
.. code-block:: javascript
   db.adminCommand( { balancerStop: 1 } )

.. include:: /includes/stop-balancer-automerger.rst

## Enable the Balancer

Use this procedure if you have disabled the balancer and are ready to re-enable it:

#. Connect to any :binary:`~bin.mongos` in the cluster using the :binary:`~bin.mongosh` shell.

#. Issue one of the following operations to enable the balancer:

From the :binary:`~bin.mongosh` shell, issue:

```javascript
   sh.startBalancer()

.. note::

   To enable the balancer from a driver, use the :command:`balancerStart`
   command against the ``admin`` database, as in the following:

   .. code-block:: javascript

      db.adminCommand( { balancerStart: 1 } )
```

.. include:: /includes/start-balancer-automerger.rst

## Disable Balancing During Backups

.. include:: /includes/fact-backup-shard

If MongoDB migrates a `chunk` during a `backup </core/backups>`, you can end with an inconsistent snapshot of your `sharded cluster`. Never run a backup while the balancer is active. To ensure that the balancer is inactive during your backup operation:

- Set the `balancing window <sharding-schedule-balancing-window>`
so that the balancer is inactive during the backup. Ensure that the backup can complete while you have the balancer disabled.

- `manually disable the balancer <sharding-balancing-disable-temporarily>`
for the duration of the backup procedure.

If you turn the balancer off while it is in the middle of a balancing round, the shut down is not instantaneous. The balancer completes the chunk move in-progress and then ceases all further balancing rounds.

Before starting a backup operation, confirm that the balancer is not active. You can use the following command to determine if the balancer is active:

```javascript
!sh.getBalancerState() && !sh.isBalancerRunning()
```

When the backup procedure is complete you can reactivate the balancer process.

## Disable Balancing on a Collection

You can disable balancing for a specific collection with the :method:`sh.disableBalancing()` method. You may want to disable the balancer for a specific collection to support maintenance operations or atypical workloads, for example, during data ingestions or data exports.

When you disable balancing on a collection, MongoDB will not interrupt in progress migrations.

To disable balancing on a collection, connect to a :binary:`~bin.mongos` with the :binary:`~bin.mongosh` shell and call the :method:`sh.disableBalancing()` method.

For example:

```javascript
sh.disableBalancing("students.grades")
```

The :method:`sh.disableBalancing()` method accepts as its parameter the full `namespace` of the collection.

## Enable Balancing on a Collection

You can enable balancing for a specific collection with the :method:`sh.enableBalancing()` method.

When you enable balancing for a collection, MongoDB will not immediately begin balancing data. However, if the data in your sharded collection is not balanced, MongoDB will be able to begin distributing the data more evenly.

To enable balancing on a collection, connect to a :binary:`~bin.mongos` with the :binary:`~bin.mongosh` shell and call the :method:`sh.enableBalancing()` method.

For example:

```javascript
sh.enableBalancing("students.grades")
```

The :method:`sh.enableBalancing()` method accepts as its parameter the full `namespace` of the collection.

## Confirm Balancing is Enabled or Disabled

To confirm whether balancing for a collection is enabled or disabled, query the `collections` collection in the `config` database for the collection `namespace` and check the `noBalance` field. For example:

```javascript
db.getSiblingDB("config").collections.findOne({_id : "students.grades"}).noBalance;
```

This operation will return a null error, `true`, `false`, or no output:

- A null error indicates the collection namespace is incorrect.
- If the result is `true`, balancing is disabled.
- If the result is `false`, balancing is enabled currently but has been
disabled in the past for the collection. Balancing of this collection will begin the next time the balancer runs.

- If the operation returns no output, balancing is enabled currently and
has never been disabled in the past for this collection. Balancing of this collection will begin the next time the balancer runs.

You can also see if the balancer is enabled using :method:`sh.status()`. The `sh.status.balancer.currently-enabled` field indicates if the balancer is enabled.

## Change Replication Behavior for Chunk Migration

### Secondary Throttle

During chunk migration, the `_secondaryThrottle` value determines when the migration proceeds with next document in the chunk.

In the `config.settings` collection:

- If the `_secondaryThrottle` setting for the balancer is set to a
`write concern`, each document moved during chunk migration must receive the requested acknowledgment before proceeding with the next document.

- If the `_secondaryThrottle` setting is unset, the migration process
does not wait for replication to a secondary and instead continues with the next document.

This is the default behavior for `WiredTiger <storage-wiredtiger>`.

To change the `_secondaryThrottle` setting, connect to a :binary:`~bin.mongos instance and directly update the secondaryThrottle` value in the `config.settings` collection of the `config database <config-database>`. For example, from a :binary:`~bin.mongosh` shell connected to a :binary:`~bin.mongos`, run the following command:

```javascript
use config
db.settings.updateOne(
   { "_id" : "balancer" },
   { $set : { "_secondaryThrottle" : { "w": "majority" }  } },
   { upsert : true }
)
```

The effects of changing the `_secondaryThrottle setting may not be immediate. To ensure an immediate effect, stop and restart the balancer to enable the selected value of secondaryThrottle`.

For more information on the replication behavior during various steps of chunk migration, see `chunk-migration-replication`.

- Use the :dbcommand:`moveRange` command's `secondaryThrottle` and
`writeConcern` options to specify the behavior during the command.

- Use the :dbcommand:`moveChunk command's secondaryThrottle` and
`writeConcern` options to specify the behavior during the command.

For details, see :dbcommand:`moveRange` and :dbcommand:`moveChunk`.

### Wait for Delete

The `_waitForDelete` setting of the balancer and the :dbcommand:`moveChunk command affects how the balancer migrates multiple chunks from a shard. Similarly, the waitForDelete` setting of the balancer and the :dbcommand:`moveRange command also affect how the balancer migrates multiple chunks from a shard. By default, the balancer does not wait for the on-going migration's delete phase to complete before starting the next chunk migration. To have the delete phase **block** the start of the next chunk migration, you can set the waitForDelete` to true.

For details on chunk migration, see `sharding-chunk-migration`. For details on the chunk migration queuing behavior, see `chunk-migration-queuing`.

> **Important:** .. include:: /includes/sharding/waitForDelete-warning.rst

To change the balancer's `_waitForDelete` value:

#. Connect to a :binary:`~bin.mongos` instance.

#. Update the `_waitForDelete` value in the `config.settings` collection of the `config database <config-database>`. For example:

```javascript
   use config
   db.settings.updateOne(
      { "_id" : "balancer" },
      { $set : { "_waitForDelete" : true } },
      { upsert : true }
   )
```

Once set to `true`, to revert to the default behavior:

#. Connect to a :binary:`~bin.mongos` instance.

#. Update or unset the `_waitForDelete` field in the `config.settings` collection of the `config database <config-database>`:

```javascript
   use config
   db.settings.updateOne(
      { "_id" : "balancer", "_waitForDelete": true },
      { $unset : { "_waitForDelete" : "" } }
   )
```

### Balance Ranges that Exceed Size Limit

By default, MongoDB cannot move a range if the number of documents in the range is greater than 2 times the result of dividing the configured `range size<sharding-range-size>` by the average document size.

By specifying the balancer setting `attemptToBalanceJumboChunks` to `true`, the balancer can migrate these large ranges as long as they have not been labeled as `jumbo <jumbo-chunk>`.

To set the balancer's `attemptToBalanceJumboChunks` setting, connect to a :binary:`~bin.mongos` instance and directly update the `config.settings` collection. For example, from a :binary:`~bin.mongosh` shell connected to a :binary:`~bin.mongos` instance, run the following command:

```javascript
db.getSiblingDB("config").settings.updateOne(
   { _id: "balancer" },
   { $set: { attemptToBalanceJumboChunks : true } },
   { upsert: true }
)
```

If the range you want to move is labeled `jumbo`, you can `manually clear the jumbo flag <clear-jumbo-flag-manually>` to have the balancer attempt to migrate the range.

You can also manually migrate ranges that exceed the size limit (with or without the `jumbo` label) using either:

- the :dbcommand:`moveRange` command with the
`forceJumbo: true <moverange-forceJumbo>` option

- the :dbcommand:`moveChunk` command with the
`forceJumbo: true <moverange-forceJumbo>` option

However, when you run :dbcommand:`moveRange` or :dbcommand:`moveChunk` with `forceJumbo: true`, write operations to the collection may block for a long period of time during the migration.
