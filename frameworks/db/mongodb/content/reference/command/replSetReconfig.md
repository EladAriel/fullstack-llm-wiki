---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetReconfig.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# replSetReconfig (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     replSetReconfig: <new_config_document>, 
     force: <boolean>,
     maxTimeMS: <int>
    }
 )
```

## Command Fields

The command takes the following optional field:

You may also run :dbcommand:`replSetReconfig` with the shell's :method:`rs.reconfig()` method.

## Behavior

### Global Write Concern

.. include:: /includes/fact-set-global-write-concern-before-reconfig.rst

### `term` Replica Configuration Field

The :rsconf:`term` field is set by the `primary` replica set member. The primary ignores the :rsconf:`term` field if set explicitly in the :dbcommand:`replSetReconfig` operation.

### Reconfiguration Can Add or Remove No More than One Voting Member at a Time

.. include:: /includes/extracts/replSetReconfig-single-node.rst

### Reconfiguration Waits Until a Majority of Members Install the Replica Configuration

.. include:: /includes/extracts/replSetReconfig-majority.rst

### Automatic Reconfiguration for New Voting Replica Set Members

.. include:: /includes/extracts/initial-sync-semantics.rst

### Access Control

To run the command on deployments that enforce `access control</core/authorization>`, the user must have :authaction:`replSetConfigure` privilege action on the cluster resource. The :authrole:`clusterManager` built-in role, available in the `admin` database, provides the required privileges for this command.

### Locking Behavior

:dbcommand:`replSetReconfig` obtains a special mutually exclusive lock to prevent more than one :dbcommand:`replSetReconfig` operation from occurring at the same time.

### Mixed Version Replica Set

> **Warning:** .. include:: /includes/warning-mixed-version-rs-config.rst

### Availability

A majority of the set's members must be operational for the changes to propagate properly.

:dbcommand:`replSetReconfig` can trigger the current primary to step down in some situations. Primary step-down triggers an `election <replica-set-elections>` to select a new `primary`:

- When the new primary steps up, it increments the :rsconf:`term` field to
distinguish configuration changes made on the new primary from changes made on the previous primary.

- When the primary steps down, it no longer
closes all client connections; however, writes that were in progress are killed. For details, see `replSetStepDown-behavior`.

.. include:: /includes/fact-election-latency.rst

During the election process, the cluster cannot accept write operations until it elects the new primary.

.. include:: /includes/fact-retryable-writes-failover-election.rst

To further reduce potential impact to a production cluster, reconfigure only during scheduled maintenance periods.

### `{ force: true }`

> **Warning:** .. include:: /includes/force-true-warning.rst

### Drop Outgoing Connections After Removing a Member

Using :dbcommand:`replSetReconfig` to remove a replica set member does not automatically drop open outgoing connections from other replica set members to the removed member.

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

.. include:: /includes/warning-no-ip-addresses-in-split-horizons.rst

### Member Priority and Votes

- .. include:: /includes/fact-rs-nonzero-priority-vote-restriction.rst
- .. include:: /includes/fact-rs-non-voting-priority-restriction.rst
## Additional Information

`replSetGetConfig-output`, `/reference/replica-configuration`, :method:`rs.reconfig()`, and :method:`rs.conf()`.
