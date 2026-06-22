---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/killOp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# killOp (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following form:

```javascript
db.adminCommand(
   { 
     killOp: 1, 
     op: <opid>, 
     comment: <any> 
   }
)
```

## Command Fields

.. include:: /includes/extracts/warning-terminating-ops-command.rst

## Behavior

Do not use :dbcommand:`killOp` to terminate an in-progress index builds in replica sets or sharded clusters. Use :dbcommand:`dropIndexes` on the `primary` to drop the index. See `dropIndexes-cmd-index-builds`.

### Access Control

On systems running with :setting:`~security.authorization`, to kill operations not owned by the user, the user must have access that includes the :authaction:`killop` privilege action.

On :binary:`~bin.mongod` instances, users can kill their own operations even without the :authaction:`killop` privilege action.

### Sharded Cluster

The :dbcommand:`killOp` command can be run on a :binary:`~bin.mongos` and can kill queries (i.e. read operations) that span shards in a cluster. The :dbcommand:`killOp` command from the :binary:`~bin.mongos` does not propagate to the shards when the operation to be killed is a write operation.

For information on how to list sharding operations that are active on a :binary:`~bin.mongos`, see the `localOps` parameter in :pipeline:`$currentOp`.

For more information and examples on killing operations on a sharded cluster, see:

- `kill-read-ops-sharded-cluster`
- `kill-write-ops-sharded-cluster`
## Example

The following example uses :dbcommand:`killOp` to target the running operation with opid `3478`.

```javascript
db.adminCommand( { "killOp": 1, "op": 3478 } )
```

The operation returns the following result:

```javascript
{ "info" : "attempting to kill op", "ok" : 1 }
```

:dbcommand:`killOp` reports success if it succeeded in marking the specified operation for termination. Operations may not actually be terminated until they reach an appropriate interruption point. Use :pipeline:`$currentOp` or :method:`db.currentOp()` to confirm the target operation was terminated.
