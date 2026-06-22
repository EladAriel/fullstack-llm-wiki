---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/renameCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# renameCollection (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

### Stable API Support

.. include:: /includes/renameCollection-stable-api-compatibility.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     renameCollection: "<source_namespace>",
     to: "<target_namespace>",
     dropTarget: <true|false>,
     writeConcern: <document>,
     comment: <any> 
   }
)
```

## Command Fields

The command contains the following fields:

## Behavior

### Sharded Collections

You can use the `renameCollection` command to change the name of a sharded collection. The target database must be the same as the source database. This operation preserves all indexes.

### Unsharded Collections

You can use `renameCollection` to rename an unsharded collection in a sharded cluster as long as the source and target databases have the same primary shard. If you run `renameCollection` to rename a collection in the same database, the operation preserves collection data and indexes. If you run `renameCollection` against a different database, the operation rewrites collection data and indexes to new files.

### Time Series Collections

You **cannot** use `renameCollection` to rename a time series collection. For more information, see `Time Series Collection Limitations <manual-timeseries-collection-limitations>`.

### Existing Target Collection

`renameCollection` fails if `target` is the name of an existing collection and you do not specify `dropTarget: true`.

### Performance

`renameCollection` has different performance implications depending on the target `namespace`.

If the target database is the same as the source database, `renameCollection` simply changes the namespace. This is a quick operation.

If the target database differs from the source database, `renameCollection` copies all documents from the source collection to the target collection. Depending on the size of the collection, this may take longer to complete.

### Resource Locking in Sharded Clusters

.. versionchanged:: 5.0

.. include:: /includes/rename-collection-in-shard.rst

For more information on locking in MongoDB, see `/faq/concurrency`.

### Resource Locking in Replica Sets

If renaming a collection within the same database, `renameCollection` obtains an exclusive lock on the source and target collections for the duration of the operation. All subsequent operations on the collections must wait until `renameCollection` completes.

If renaming a collection between different databases, `renameCollection` obtains an exclusive (W) lock on the target database, an intent shared (r) lock on the source database, and a shared (S) lock on the source collection. Subsequent operations on the target database must wait until `renameCollection` releases the exclusive database lock.

For more information on locking in MongoDB, see `/faq/concurrency`.

### `local` Database

- You cannot rename a collection from a replicated database to the
`local` database, which is not replicated.

- You cannot rename a collection from the `local` database, which is
not replicated, to a replicated database.

### Open Cursors and Change Streams

.. include:: /includes/warning-renamecollection-cursors-changestreams.rst

### Interaction with `mongodump`

A :binary:`~bin.mongodump` started with :option:`--oplog <mongodump.--oplog>` fails if a client issues the `renameCollection` command during the dump process. See :option:`mongodump.--oplog` for more information.

## Example

The following example renames a collection named `orders` in the `test` database to `orders2014` in the `test` database.

```javascript
db.adminCommand( { renameCollection: "test.orders", to: "test.orders2014" } )
```

:binary:`~bin.mongosh` provides the :method:`db.collection.renameCollection()` helper for the command to rename collections within the same database. The following is equivalent to the previous example:

```javascript
use test
db.orders.renameCollection( "orders2014" )
```
