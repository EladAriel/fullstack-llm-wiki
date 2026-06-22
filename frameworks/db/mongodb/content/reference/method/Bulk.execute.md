---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.execute.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Bulk.execute() (mongosh method)

> **Tip:** MongoDB also provides :method:`db.collection.bulkWrite()` for
performing bulk write operations.

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Behavior

### Ordered Operations

.. include:: /includes/fact-bulk-operation-ordered-list.rst

.. include:: /includes/fact-bulk-operation-batches.rst

.. include:: /includes/fact-bulk-operation-sharded-cluster.rst

### Unordered Operations

.. include:: /includes/fact-bulk-operation-unordered-list.rst

.. include:: /includes/fact-bulk-operation-batches.rst

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

For :method:`Bulk.insert()` operations, the collection must already exist.

For :method:`Bulk.find.upsert()`, if the operation results in an upsert, the collection must already exist.

.. include:: /includes/extracts/transactions-operations-write-concern.rst

.. include:: /includes/extracts/transactions-usage.rst

## Examples

### Execute Bulk Operations

The following initializes a :method:`Bulk()` operations builder on the `items` collection, adds a series of insert operations, and executes the operations:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.insert( { item: "abc123", status: "A", defaultQty: 500, points: 5 } );
bulk.insert( { item: "ijk123", status: "A", defaultQty: 100, points: 10 } );
bulk.execute( );
```

The operation returns the following :method:`BulkWriteResult()` object:

```javascript
BulkWriteResult({
  acknowledged: true,
  insertedCount: 2,
  insertedIds: {
    '0': ObjectId("64e61e3b84ff8808cd43a92c"),
    '1': ObjectId("64e61e3b84ff8808cd43a92d")
  },
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 0,
  upsertedCount: 0,
  upsertedIds: {}
})
```

For details on the return object, see :method:`BulkWriteResult()`. For details on the batches executed, see :method:`Bulk.getOperations()`.

### Override Default Write Concern

The following operation to a replica set specifies a `write concern <write-concern>` of `"w: 1"` with a `wtimeout` of 5000 milliseconds such that the method returns after the writes propagate to a majority of the voting replica set members or the method times out after five seconds.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.insert( { item: "efg123", status: "A", defaultQty: 100, points: 0 } );
bulk.insert( { item: "xyz123", status: "A", defaultQty: 100, points: 0 } );
bulk.execute( { w: 1, wtimeout: 5000 } );
```

The operation returns the following :method:`BulkWriteResult()` object:

```javascript
BulkWriteResult({
  acknowledged: true,
  insertedCount: 2,
  insertedIds: {
    '0': ObjectId("64e61e3b84ff8808cd43a92c"),
    '1': ObjectId("64e61e3b84ff8808cd43a92d")
  },
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 0,
  upsertedCount: 0,
  upsertedIds: {}
})
```
