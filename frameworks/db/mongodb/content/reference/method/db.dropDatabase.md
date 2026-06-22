---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.dropDatabase.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# db.dropDatabase() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The :method:`db.dropDatabase()` method takes an optional parameter:

## Behavior

The :method:`db.dropDatabase()` wraps the :dbcommand:`dropDatabase` command.

### Locks

The operation takes an exclusive (X) database lock only.

### User Management

.. include:: /includes/fact-drop-database-users.rst

### Indexes

.. include:: /includes/extracts/4.4-changes-drop-database-in-progress-indexes.rst

.. include:: /includes/fact-abort-index-build-replica-sets.rst

### Replica Set and Sharded Clusters

Replica Sets At minimum, :method:`db.dropDatabase()` waits until all collection drops in the database have propagated to a majority of the replica set members (i.e. uses the write concern :writeconcern:`"majority"`).

You can specify a write concern to the method. If you specify a write concern that requires acknowledgment from fewer than the majority, the method uses write concern :writeconcern:`"majority"`.

If you specify a write concern that requires acknowledgment from more than the majority, the method uses the specified write concern.

Sharded Clusters

.. include:: /includes/extracts/mongos-operations-wc-drop-database.rst

### Change Streams

The :method:`db.dropDatabase()` method and :dbcommand:`dropDatabase` command create an `change-event-invalidate` for any `/changeStreams` opened on the dropped database or opened on the collections in the dropped database.

## Example

The following example in :binary:`~bin.mongosh` uses the `use <database>` operation to switch the current database to the `temp` database and then uses the :method:`db.dropDatabase()` method to drop the `temp` database:

```javascript
use temp
db.dropDatabase()
```

> **Seealso:** :dbcommand:`dropDatabase`
