---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/replication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========

# Replication

A replica set in MongoDB is a group of :binary:`~bin.mongod` processes that maintain the same data set. Replica sets provide redundancy and `high availability`, and are the basis for all production deployments. This section introduces replication in MongoDB and the components and architecture of replica sets. The section also provides tutorials for common tasks related to replica sets.

## Redundancy and Data Availability

Replication provides redundancy and `data availability <high availability>`, maintaining multiple copies of data across database servers to tolerate the loss of any single server.

In some cases, replication can provide increased read capacity as clients can send read operations to different servers. Maintaining copies of data in different data centers can increase data locality and availability for distributed applications. You can also maintain additional copies for dedicated purposes, such as disaster recovery, reporting, or backup.

## Replication in MongoDB

A replica set is a group of :binary:`~bin.mongod` instances that maintain the same data set. A replica set contains several data bearing nodes and optionally one arbiter node. Of the data bearing nodes, one and only one member is deemed the primary node, while the other nodes are deemed secondary nodes.

.. include:: /includes/replica-set-nodes-cannot-be-shared.rst

The `primary node <replica-set-primary>` receives all write operations. A replica set can have only one primary capable of confirming writes with :writeconcern:`{ w: "majority" } <"majority">` write concern, although in some circumstances, another mongod instance may transiently believe itself to also be primary. [#edge-cases-2-primaries]_ The primary records all changes to its data sets in its operation log, that is, the `oplog </core/replica-set-oplog>`. For more information on primary node operation, see `/core/replica-set-primary`.

.. include:: /images/replica-set-read-write-operations-primary.rst

The `secondaries <replica-set-secondary-members-ref>` replicate the primary's oplog and apply the operations to their data sets such that the secondaries' data sets reflect the primary's data set. If the primary is unavailable, an eligible secondary holds an election to select a new primary. For more information on secondary members, see `/core/replica-set-secondary`.

.. include:: /images/replica-set-primary-with-two-secondaries.rst

If cost constraints prevent adding another secondary, you may add a :binary:`~bin.mongod` instance to a replica set as an `arbiter <replica-set-arbiter-configuration>`. An arbiter participates in `elections <replica-set-elections>` but does not hold data (that is, does not provide data redundancy). For more information on arbiters, see `/core/replica-set-arbiter`.

.. include:: /images/replica-set-primary-with-secondary-and-arbiter.rst

An `arbiter <replica-set-arbiter-configuration>` is always an arbiter whereas a `primary <replica-set-primary>` may step down and become a `secondary <replica-set-secondary-members-ref>` and a secondary may become the primary during an election.

## Asynchronous Replication

Secondaries replicate the primary's oplog and apply the operations to their data sets asynchronously. By having the secondaries' data sets reflect the primary's data set, the replica set can continue to function despite the failure of one or more members.

For more information on replication mechanics, see `replica-set-oplog` and `replica-set-sync`.

### Slow Operations

.. include:: /includes/extracts/4.2-changes-slow-oplog-log-message-footnote.rst

### Replication Lag and Flow Control

`Replication lag <replication lag>` is a delay between an operation on the `primary` and the application of that operation from the `oplog` to the `secondary`. Some small delay period may be acceptable, but significant problems emerge as replication lag grows, including building cache pressure on the primary.

.. include:: /includes/extracts/4.2-changes-flow-control-general-desc.rst

.. include:: /includes/extracts/4.2-changes-flow-control-specific-desc.rst

For more information, see `replica-set-replication-lag` and `flow-control`.

## Automatic Failover

When a primary does not communicate with the other members of the set for more than the configured :rsconf:`~settings.electionTimeoutMillis` period (10 seconds by default), an eligible secondary calls for an election to nominate itself as the new primary.

.. include:: /images/replica-set-trigger-election.rst

.. include:: /includes/fact-election-latency.rst

Lowering the :rsconf:`~settings.electionTimeoutMillis` replication configuration option from the default `10000` (10 seconds) can result in faster detection of primary failure. However, the cluster may call elections more frequently due to factors such as temporary network latency even if the primary is otherwise healthy. This can result in increased `rollbacks <replica-set-rollback>` for `w : 1 <wc-w>` write operations.

.. include:: /includes/fact-retryable-writes-failover-election.rst

MongoDB provides `mirrored reads <mirrored-reads>` to pre-warm electable secondary members' cache with the most recently accessed data. Pre-warming the cache of a secondary can help restore performance more quickly after an election.

To learn more about MongoDB's failover process, see:

- `replica-set-elections`
- `retryable-writes`
- `replica-set-rollback`
## Read Operations

### Read Preference

By default, clients read from the primary [#edge-cases-2-primaries]_; however, clients can specify a `read preference </core/read-preference>` to send read operations to secondaries.

.. include:: /images/replica-set-read-preference-secondary.rst

`Asynchronous replication <asynchronous-replication>` to secondaries means that reads from secondaries may return data that does not reflect the state of the data on the primary.

.. include:: /includes/extracts/transactions-read-pref.rst

For information on reading from replica sets, see `/core/read-preference`.

### Data Visibility

.. include:: /includes/extracts/concurrent-operations-read-uncommitted.rst

For more information on read isolations, consistency and recency for MongoDB, see `/core/read-isolation-consistency-recency`.

### Mirrored Reads

Mirrored reads reduce the impact of primary elections by pre-warming the caches of :rsconf:`electable <members[n].priority>` secondary replica set members before a failover occurs. The primary mirrors a sample of the `supported operations <mirrored-reads-supported-operations>` it receives to electable secondaries.

The size of the subset of :rsconf:`electable <members[n].priority>` secondary replica set members that receive mirrored reads can be configured with the :parameter:`mirrorReads <mirrorReads>` parameter. See `Enable/Disable Support for Mirrored Reads <mirrored-reads-parameters>` for further details.

> **Note:** Mirrored reads do not affect the primary's response to the client.
The reads that the primary mirrors to secondaries are
"fire-and-forget" operations. The primary doesn't await responses.

Targeted Mirrored Reads ```````````````````````

.. include:: /includes/sharding/targeted-mirror-reads-overview.rst

Supported Operations ````````````````````

Mirrored reads support the following operations:

- :dbcommand:`count`
- :dbcommand:`distinct`
- :dbcommand:`find`
- :dbcommand:`findAndModify` (Specifically, the filter is sent as a
mirrored read)

- :dbcommand:`update` (Specifically, the filter is sent as a mirrored
read)

Enable/Disable Support for Mirrored Reads `````````````````````````````````````````

Mirrored reads are enabled by default and use a default :parameter:`sampling rate <mirrorReads>` of `0.01`. To disable mirrored reads, set the :parameter:`mirrorReads` parameter to `{ samplingRate: 0.0 }`:

```javascript
db.adminCommand( {
  setParameter: 1,
  mirrorReads: { samplingRate: 0.0 }
} )
```

With a sampling rate greater than `0.0`, the primary mirrors `supported reads <mirrored-reads-supported-operations>` to a subset of :rsconf:`electable <members[n].priority>` secondaries. With a sampling rate of `0.01`, the primary mirrors one percent of the supported reads it receives to a selection of electable secondaries.

For example, consider a replica set that consists of one primary and two electable secondaries. If the primary receives `1000` operations that can be mirrored and the sampling rate is `0.01`, the primary mirrors about `10` supported reads to a randomly chosen selection of electable secondaries.

Change the Sampling Rate for Mirrored Reads ```````````````````````````````````````````

To change the sampling rate for mirrored reads, set the :parameter:`mirrorReads` parameter to a number between `0.0` and `1.0`:

- A sampling rate of `0.0` disables mirrored reads.
- A sampling rate of a number between `0.0` and `1.0` results in
the primary forwarding a random sample of the `supported reads <mirrored-reads-supported-operations>` at the specified sample rate to electable secondaries.

- A sampling rate of `1.0` results in the primary forwarding all
`supported reads <mirrored-reads-supported-operations>` to electable secondaries.

For details, see :parameter:`mirrorReads`.

Mirrored Reads Metrics ``````````````````````

The :dbcommand:`serverStatus` command and the :method:`db.serverStatus()` shell method return :serverstatus:`mirroredReads` metrics if you specify the field in the operation:

```javascript
db.serverStatus( { mirroredReads: 1 } )
```

## Transactions

`Multi-document transactions <transactions>` are available for replica sets.

.. include:: /includes/extracts/transactions-read-pref.rst

.. include:: /includes/extracts/transactions-committed-visibility.rst

## Change Streams

`Change streams <changeStreams>` are available for replica sets and sharded clusters. Change streams allow applications to access real-time data changes without the complexity and risk of tailing the oplog. Applications can use change streams to subscribe to all data changes on a collection or collections.

## Additional Features

Replica sets provide a number of options to support application needs. For example, you may deploy a replica set with `members in multiple data centers </core/replica-set-architecture-geographically-distributed>`, or control the outcome of elections by adjusting the :rsconf:`members[n].priority` of some members. Replica sets also support dedicated members for reporting, disaster recovery, or backup functions.

See `replica-set-secondary-only-members`, `replica-set-hidden-members` and `replica-set-delayed-members` for more information.

.. include:: /includes/footnote-two-primaries-edge-cases.rst

## Contents

- Oplog </core/replica-set-oplog>
- Data Synchronization </core/replica-set-sync>
- Replica Set Members </core/replica-set-members>
- Deployment Architectures </core/replica-set-architectures>
- High Availability </core/replica-set-high-availability>
- Read & Write Semantics </applications/replication>
- Troubleshoot </tutorial/troubleshoot-replica-sets>
- local Database </reference/local-database>
