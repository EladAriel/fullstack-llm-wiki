---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.tojson.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Bulk.toJSON() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

The following initializes a :method:`Bulk()` operations builder on the `items` collection, adds a series of write operations, and calls :method:`Bulk.toJSON()` on the `bulk` builder object.

```javascript
var bulk = db.items.initializeOrderedBulkOp();
bulk.insert( { item: "abc123", status: "A", defaultQty: 500, points: 5 } );
bulk.insert( { item: "ijk123", status: "A", defaultQty: 100, points: 10 } );
bulk.find( { status: "D" } ).deleteOne();
bulk.toJSON();
```

The :method:`Bulk.toJSON()` returns the following JSON document

```javascript
{
  acknowledged: true,
  insertedCount: 2,
  insertedIds: [
    { index: 0, _id: ObjectId("627bf77e5e19ff3518448887") },
    { index: 1, _id: ObjectId("627bf77e5e19ff3518448888") }
  ],
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 0,
  upsertedCount: 0,
  upsertedIds: []
}
```

> **Seealso:** :method:`Bulk()`
