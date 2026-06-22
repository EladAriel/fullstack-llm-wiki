---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.initializeOrderedBulkOp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================================

# db.collection.initializeOrderedBulkOp() (mongosh method)

.. include:: /includes/fact-bulkwrite.rst

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Behavior

### Order of Operation

With an ordered operations list, MongoDB executes the write operations in the list serially.

### Execution of Operations

.. include:: /includes/fact-bulk-operation-ordered-list.rst

.. include:: /includes/fact-bulk-operation-batches.rst

.. include:: /includes/fact-bulk-operation-sharded-cluster.rst

### Error Handling

If an error occurs during the processing of one of the write operations, MongoDB will return without processing any remaining write operations in the list.

## Examples

The following initializes a :method:`Bulk()` operations builder on the `users` collection, adds a series of write operations, and executes the operations:

```javascript
var bulk = db.users.initializeOrderedBulkOp();
bulk.insert( { user: "abc123", status: "A", points: 0 } );
bulk.insert( { user: "ijk123", status: "A", points: 0 } );
bulk.insert( { user: "mop123", status: "P", points: 0 } );
bulk.find( { status: "D" } ).delete();
bulk.find( { status: "P" } ).update( { $set: { comment: "Pending" } } );
bulk.execute();
```

> **Seealso:** - :method:`db.collection.initializeUnorderedBulkOp()`
- :method:`Bulk.find()`
- :method:`Bulk.find.removeOne()`
- :method:`Bulk.execute()`
