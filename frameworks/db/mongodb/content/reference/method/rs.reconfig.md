---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.reconfig.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# rs.reconfig() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Global Write Concern

.. include:: /includes/fact-set-global-write-concern-before-reconfig.rst

### `term` Replica Configuration Field

The :rsconf:`term` field is set by the `primary` replica set member. The primary ignores the :rsconf:`term` field if set explicitly in the :method:`rs.reconfig()` operation.

### Reconfiguration Can Add or Remove No More than One Voting Member at a Time

.. include:: /includes/extracts/replSetReconfig-single-node.rst

### Reconfiguration Waits Until a Majority of Members Install the Replica Configuration

.. include:: /includes/extracts/replSetReconfig-majority.rst

### Access Control

To run the method on deployments that enforce `access control</core/authorization>`, the user must have :authaction:`replSetConfigure` privilege action on the cluster resource. The :authrole:`clusterManager` built-in role, available in the `admin` database, provides the required privileges for this command.

### Locking Behavior

:method:`rs.reconfig()` obtains a special mutually exclusive lock to prevent more than one :method:`rs.reconfig()` operation from occurring at the same time.

### Mixed Version Replica Set

> **Warning:** .. include:: /includes/warning-mixed-version-rs-config.rst

### Availability

The :method:`rs.reconfig()` shell method can trigger the current primary to step down in some situations. Primary step-down triggers an `election <replica-set-elections>` to select a new `primary`:

When the primary steps down, it stops any in-progress writes. For details, see `replSetStepDown-behavior`.

.. include:: /includes/fact-election-latency.rst

During the election process, the cluster cannot accept write operations until it elects the new primary.

.. include:: /includes/fact-retryable-writes-failover-election.rst

To further reduce potential impact to a production cluster, reconfigure only during scheduled maintenance periods.

### `{ force: true }`

> **Warning:** .. include:: /includes/force-true-warning.rst

### Member Priority and Votes

- .. include:: /includes/fact-rs-nonzero-priority-vote-restriction.rst
- .. include:: /includes/fact-rs-non-voting-priority-restriction.rst
### Drop Outgoing Connections After Removing a Member

.. This behavior will change once SERVER-36417 closes.

Using :method:`rs.reconfig()` to remove a replica set member does not automatically drop open outgoing connections from other replica set members to the removed member.

By default, replica set members wait for 5 minutes before dropping connections to the removed member. In sharded replica sets, you can modify this timeout using the :parameter:`ShardingTaskExecutorPoolHostTimeoutMS` server parameter.

To immediately drop all outgoing connections from the replica set to the removed member, run the :dbcommand:`dropConnections` administrative command on each remaining member on the replica set:

```javascript
db.adminCommand( 
  {
    "dropConnections" : 1,
    "hostAndPort" : [
      "<hostname>:<port>"
    ] 
  } 
)
```

Replace `<hostname>` and `<port>` with those of the removed member.

### Automatic Reconfiguration for New Voting Replica Set Members

.. include:: /includes/extracts/initial-sync-semantics.rst

## Examples

A replica set named `rs0` has the following configuration:

```javascript
{
   "_id" : "rs0",
   "version" : 1,
   "protocolVersion" : Long(1),
   "members" : [
      {
         "_id" : 0,
         "host" : "mongodb0.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      },
      {
         "_id" : 1,
         "host" : "mongodb1.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      },
      {
         "_id" : 2,
         "host" : "mongodb2.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      }
   ],
   "settings" : {
      "chainingAllowed" : true,
      "heartbeatIntervalMillis" : 2000,
      "heartbeatTimeoutSecs" : 10,
      "electionTimeoutMillis" : 10000,
      "catchUpTimeoutMillis" : 2000,
      "getLastErrorModes" : {

      },
      "getLastErrorDefaults" : {
         "w" : 1,
         "wtimeout" : 0
      },
      "replicaSetId" : ObjectId("58858acc1f5609ed986b641b")
   }
}
```

### Change Replica Set Member Priority

The following sequence of operations updates the :rsconf:`members[n].priority` of the second member. The operations are issued through a :binary:`~bin.mongosh` session that is connected to the primary.

```javascript
cfg = rs.conf();
cfg.members[1].priority = 2;
rs.reconfig(cfg);
```

#. The first statement uses the :method:`rs.conf()` method to retrieve a document containing the current `configuration <replSetGetConfig-output>` for the replica set and sets the document to the local variable `cfg`.

#. The second statement sets a :rsconf:`members[n].priority` value to the second document in the :rsconf:`members` array. For additional settings, see `replica set configuration settings <replSetGetConfig-output>`.

To access the member configuration document in the array, the statement uses the array index and **not** the replica set member's :rsconf:`members[n]._id` field.

#. The last statement calls the :method:`rs.reconfig()` method with the modified `cfg` to initialize this new configuration. Upon successful reconfiguration, the replica set configuration will resemble the following:

```javascript
{
   "_id" : "rs0",
   "version" : 2,
   "protocolVersion" : Long(1),
   "members" : [
      {
         "_id" : 0,
         "host" : "mongodb0.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      },
      {
         "_id" : 1,
         "host" : "mongodb1.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 2,
         "tags" : {

         },
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      },
      {
         "_id" : 2,
         "host" : "mongodb2.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      }
   ],
   "settings" : {
      "chainingAllowed" : true,
      "heartbeatIntervalMillis" : 2000,
      "heartbeatTimeoutSecs" : 10,
      "electionTimeoutMillis" : 10000,
      "catchUpTimeoutMillis" : 2000,
      "getLastErrorModes" : {

      },
      "getLastErrorDefaults" : {
         "w" : 1,
         "wtimeout" : 0
      },
      "replicaSetId" : ObjectId("58858acc1f5609ed986b641b")
   }
}
```

### Change Replica Set Settings

You can also modify the cluster replica set :rsconf:`settings` document. The :rsconf:`settings` document contains configuration options that apply to the whole replica set.

The following sequence of operations updates the :rsconf:`settings.heartbeatTimeoutSecs` of the cluster to `15`. The operations are issued through a :binary:`~bin.mongosh` session that is connected to the primary.

```javascript
cfg = rs.conf();
cfg.settings.heartbeatTimeoutSecs = 15;
rs.reconfig(cfg);
```

> **Seealso:** - :method:`rs.conf()`
- `replSetGetConfig-output`
- `/administration/replica-set-member-configuration`
- `/administration/replica-set-maintenance`
