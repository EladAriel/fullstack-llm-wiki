---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.renameCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# db.collection.renameCollection() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-renameCollection.rst

## Definition

### Parameters

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

### Stable API Support

.. include:: /includes/renameCollection-stable-api-compatibility.rst

## Behavior

The `db.collection.renameCollection()` method operates within a collection by changing the metadata associated with a given collection.

Refer to the documentation :dbcommand:`renameCollection` for additional warnings and messages.

.. include:: /includes/warning-renamecollection-cursors-changestreams.rst

- The method has the following limitations:
- `db.collection.renameCollection()` cannot move a collection
between databases. Use :dbcommand:`renameCollection` for these rename operations.

- .. include:: /includes/extracts/views-unsupported-rename.rst
- `db.collection.renameCollection()` is not supported on
`time series collections <time series collection>`.

- You cannot rename a collection to itself. If you try to rename a
collection to itself an `IllegalOperation` error is thrown.

### Resource Locking in Sharded Clusters

.. versionchanged:: 5.0

.. include:: /includes/rename-collection-in-shard.rst

For more information on locking in MongoDB, see `/faq/concurrency`.

### Resource Locking in Replica Sets

:method:`~db.collection.renameCollection()` obtains an exclusive lock on the source and target collections for the duration of the operation. All subsequent operations on the collections must wait until :method:`~db.collection.renameCollection()` completes.

### Interaction with `mongodump`

A :binary:`~bin.mongodump` started with :option:`--oplog <mongodump.--oplog>` fails if a client issues `db.collection.renameCollection()` during the dump process. See :option:`mongodump.--oplog` for more information.

## Example

Call the `db.collection.renameCollection()` method on a collection object. For example:

```javascript
db.rrecord.renameCollection("record")
```

This operation will rename the `rrecord` collection to `record`. If the target name (i.e. `record`) is the name of an existing collection, then the operation will fail.
