---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.initializeUnorderedBulkOp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================================

# db.collection.initializeUnorderedBulkOp() (mongosh method)

.. include:: /includes/fact-bulkwrite.rst

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Behavior

### Order of Operation

With an unordered operations list, MongoDB can execute in parallel the write operations in the list and in any order. If the order of operations matter, use :method:`db.collection.initializeOrderedBulkOp()` instead.

### Execution of Operations

.. include:: /includes/fact-bulk-operation-unordered-list.rst

.. include:: /includes/fact-bulk-operation-batches.rst

### Error Handling

If an error occurs during the processing of one of the write operations, MongoDB will continue to process remaining write operations in the list.

## Example

The following initializes a :method:`Bulk()` operations builder and adds a series of insert operations to add multiple documents:

```javascript
var bulk = db.users.initializeUnorderedBulkOp();
bulk.insert( { user: "abc123", status: "A", points: 0 } );
bulk.insert( { user: "ijk123", status: "A", points: 0 } );
bulk.insert( { user: "mop123", status: "P", points: 0 } );
bulk.execute();
```

> **Seealso:** - :method:`db.collection.initializeOrderedBulkOp()`
- :method:`Bulk()`
- :method:`Bulk.insert()`
- :method:`Bulk.execute()`
