---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/troubleshoot-replica-sets.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# Troubleshoot Replica Sets

This section describes common strategies for troubleshooting `replica set` deployments.

## Check Replica Set Status

To display the current state of the replica set and current state of each member, run the :method:`rs.status()` method in a :binary:`~bin.mongosh` session that is connected to the replica set's `primary`. For descriptions of the information displayed by :method:`rs.status()`, see `/reference/command/replSetGetStatus`.

> **Note:** The :method:`rs.status()` method is a wrapper that runs the
:dbcommand:`replSetGetStatus` database command.

## Check the Replication Lag

Replication lag is a delay between an operation on the `primary` and the application of that operation from the `oplog` to the `secondary`. Replication lag can be a significant issue and can seriously affect MongoDB `replica set` deployments. Excessive replication lag makes "lagged" members ineligible to quickly become primary and increases the possibility that distributed read operations will be inconsistent.

To check the current length of replication lag:

- In a :binary:`~bin.mongosh` session that is connected to the primary,
call the :method:`rs.printSecondaryReplicationInfo()` method.

Returns the `syncedTo` value for each member, which shows the time when the last oplog entry was written to the secondary, as shown in the following example:

```none
  source: m1.example.net:27017
      syncedTo: Thu Apr 10 2014 10:27:47 GMT-0400 (EDT)
      0 secs (0 hrs) behind the primary 
  source: m2.example.net:27017
      syncedTo: Thu Apr 10 2014 10:27:47 GMT-0400 (EDT)
      0 secs (0 hrs) behind the primary 

A :ref:`delayed member <replica-set-delayed-members>` may show as ``0``
seconds behind the primary when the inactivity period on the primary is
greater than the :rsconf:`members[n].secondaryDelaySecs`
value.

.. note::

  The :method:`rs.status()` method is a wrapper around the
  :dbcommand:`replSetGetStatus` database command.

.. include:: /includes/fact-totalOplogSlotDurationMicros.rst

.. example::

  .. include:: /includes/fact-totalOplogSlotDurationMicrosExample.rst
```

- Monitor the rate of replication by checking for non-zero or increasing
oplog time values in the :guilabel:`Replication Lag` graph available in [Cloud Manager](https://docs.cloudmanager.mongodb.com/reference/alerts/replication-lag/) and in [Ops Manager](https://docs.opsmanager.mongodb.com/current/reference/alerts/replication-lag/).

.. include:: /includes/replacement-mms.rst

### Replication Lag Causes

Possible causes of replication lag include:

- **Network Latency**
Check the network routes between the members of your set to ensure that there is no packet loss or network routing issue.

Use tools including `ping` to test latency between set members and `traceroute` to expose the routing of packets network endpoints.

- **Disk Throughput**
If the file system and disk device on the secondary is unable to flush data to disk as quickly as the primary, then the secondary will have difficulty keeping state. Disk-related issues are incredibly prevalent on multi-tenant systems, including virtualized instances, and can be transient if the system accesses disk devices over an IP network (as is the case with Amazon's EBS system.)

Use system-level tools to assess disk status, including `iostat` or `vmstat`.

- **Concurrency**
In some cases, long-running operations on the primary can block replication on secondaries. For best results, configure `write concern <wc-w>` to require confirmation of replication to secondaries. This prevents write operations from returning if replication cannot keep up with the write load.

You can also use the `database profiler` to see if there are slow queries or long-running operations that correspond to the incidences of lag.

- **Appropriate Write Concern**
If you are performing a large data ingestion or bulk load operation that requires a large number of writes to the primary, particularly with :writeconcern:`unacknowledged write concern <\<number\>>`, the secondaries will not be able to read the oplog fast enough to keep up with changes.

To prevent this, request `write acknowledgment write concern </reference/write-concern>` after every 100, 1,000, or another interval to provide an opportunity for secondaries to catch up with the primary.

For more information see:

- `Write Concern <wc-w>`
- `Replica Set Write Concern <write-operations-replica-sets>`
- `replica-set-oplog-sizing`
### Flow Control

.. include:: /includes/extracts/4.2-changes-flow-control-general-desc.rst

.. include:: /includes/extracts/4.2-changes-flow-control-specific-desc.rst

Replication lag can occur without the replica set receiving sufficient load to engage flow control, such as in the case of an unresponsive `secondary`.

To view the status of flow control, run the following commands on the `primary`:

#. Run the :method:`rs.printSecondaryReplicationInfo` method to determine if any nodes are lagging:

```javascript
   rs.printSecondaryReplicationInfo()    

Example output:

.. code-block:: javascript 
   :copyable: false

   source: 192.0.2.2:27017
   {
     syncedTo: 'Mon Jan 31 2022 18:58:50 GMT+0000 (Coordinated Universal Time)',
     replLag: '0 secs (0 hrs) behind the primary '
   }
   ---
   source: 192.0.2.3:27017
   {
     syncedTo: 'Mon Jan 31 2022 18:58:05 GMT+0000 (Coordinated Universal Time)',
     replLag: '45 secs (0 hrs) behind the primary '
   }
```

#. Run the :dbcommand:`serverStatus` command and use the :serverstatus:`flowControl.isLagged` value to determine whether the replica set has engaged flow control:

```javascript
   db.runCommand( { serverStatus: 1 } ).flowControl.isLagged     

Example output:

.. code-block:: javascript
   :copyable: false

   false

If flow control has not engaged, investigate the :term:`secondary`
to determine the cause of the replication lag, such as limitations in 
the hardware, network, or application.
```

For information on flow control statistics, see:

- :serverstatus:`flowControl <flowControl>`
- `$currentOp.waitingForFlowControl` and `$currentOp.flowControlStats`
- `currentOp.waitingForFlowControl` and `currentOp.flowControlStats`
## Slow Application of Oplog Entries

.. include:: /includes/extracts/4.2-changes-slow-oplog-log-message-footnote.rst

## Test Connections Between all Members

All members of a `replica set` must be able to connect to every other member of the set to support replication. Always verify connections in both "directions."  Networking topologies and firewall configurations can prevent normal and required connectivity, which can block replication.

.. include:: /includes/fact-default-bind-ip.rst

Consider the following example of a bidirectional test of networking:

## Socket Exceptions when Rebooting More than One Secondary

When you reboot members of a replica set, ensure that the set is able to elect a primary during the maintenance. This means ensuring that a majority of the set's :rsconf:`members[n].votes` are available.

When a set's active members can no longer form a majority, the set's `primary` steps down and becomes a `secondary`.  The primary does not close client connections when it steps down.

Clients cannot write to the replica set until the members elect a new primary.

For more information on votes, see `/core/replica-set-elections`. For related information on connection errors, see `faq-keepalive`.

## Check the Size of the Oplog

A larger `oplog` can give a replica set a greater tolerance for lag, and make the set more resilient.

To check the size of the oplog for a given `replica set` member, connect to the member in :binary:`~bin.mongosh` and run the :method:`rs.printReplicationInfo()` method.

The output displays the size of the oplog and the date ranges of the operations contained in the oplog. In the following example, the oplog is about 10 MB and is able to fit about 26 hours (94400 seconds) of operations:

```javascript
configured oplog size:   10.10546875MB
log length start to end: 94400 (26.22hrs)
oplog first event time:  Mon Mar 19 2012 13:50:38 GMT-0400 (EDT)
oplog last event time:   Wed Oct 03 2012 14:59:10 GMT-0400 (EDT)
now:                     Wed Oct 03 2012 15:00:21 GMT-0400 (EDT)
```

The oplog should be long enough to hold all transactions for the longest downtime you expect on a secondary. [#oplog]_ At a minimum, an oplog should be able to hold minimum 24 hours of operations; however, many users prefer to have 72 hours or even a week's work of operations.

For more information on how oplog size affects operations, see:

- `replica-set-oplog-sizing`,
- `replica-set-delayed-members`, and
- `replica-set-replication-lag`.
> **Note:** members. If you resize the oplog, resize it on all members.

To change oplog size, see the `/tutorial/change-oplog-size` tutorial.

.. include:: /includes/fact-oplog-size.rst
