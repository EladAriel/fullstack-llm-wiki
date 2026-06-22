---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.update.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Bulk.find.update() (mongosh method)

.. include:: /includes/fact-bulkwrite.rst

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

The following example initializes a :method:`Bulk()` operations builder for the `items` collection, and adds various `multi` update operations to the list of operations.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "D" } ).update( { $set: { status: "I", points: "0" } } );
bulk.find( { item: null } ).update( { $set: { item: "TBD" } } );
bulk.execute();
```

### Update with Aggregation Pipeline

Update methods can accept an aggregation pipeline. For example, the following uses:

- the :pipeline:`$set` stage which can provide similar
behavior to the :update:`$set` update operator expression,

- the aggregation variable :variable:`NOW`, which resolves to the
current datetime and can provide similar behavior to a :update:`$currentDate` update operator expression. To access aggregation variables, prefix the variable with double dollar signs `$$` and enclose in quotes.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "P" } ).update(
   [  
      { $set: { points: 0, lastModified: "$$NOW" } }
   ]
);
bulk.execute();
```

> **Seealso:** - :method:`db.collection.initializeUnorderedBulkOp()`
- :method:`db.collection.initializeOrderedBulkOp()`
- :method:`Bulk.find()`
- :method:`Bulk.find.updateOne()`
- :method:`Bulk.execute()`
- `All Bulk Methods <bulk-methods>`
