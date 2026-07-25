---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/dropDatabase.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================

# dropDatabase (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {   
     dropDatabase: 1, 
     writeConcern: <document>, 
     comment: <any> 
   }
)
```

## Command Fields

The command takes the following optional fields:

:binary:`~bin.mongosh` also provides the helper method :method:`db.dropDatabase()`.

## Behavior

### Locks

The operation takes an exclusive (X) database lock only.

### User Management

.. include:: /includes/fact-drop-database-users.rst

### Indexes

.. include:: /includes/extracts/4.4-changes-drop-database-in-progress-indexes.rst

.. include:: /includes/fact-abort-index-build-replica-sets.rst

### Replica Set and Sharded Clusters

Replica Sets At minimum, :dbcommand:`dropDatabase` waits until all collections drops in the database have propagated to a majority of the replica set members (i.e. uses the write concern :writeconcern:`"majority"`).

If you specify a write concern that requires acknowledgment from fewer than the majority, the command uses write concern :writeconcern:`"majority"`.

If you specify a write concern that requires acknowledgment from more than the majority, the command uses the specified write concern.

Sharded Clusters

.. include:: /includes/extracts/mongos-operations-wc-drop-database.rst

### Change Streams

The :method:`db.dropDatabase()` method and :dbcommand:`dropDatabase` create an `change-event-invalidate` for any `/changeStreams` opened on the dropped database or opened on the collections in the dropped database.

## Example

The following example in :binary:`~bin.mongosh` uses the `use <database>` operation to switch the current database to the `temp` database and then uses the :dbcommand:`dropDatabase` command to drop the `temp` database:

```javascript
use temp
db.runCommand( { dropDatabase: 1 } )
```

> **Seealso:** :dbcommand:`dropAllUsersFromDatabase`
