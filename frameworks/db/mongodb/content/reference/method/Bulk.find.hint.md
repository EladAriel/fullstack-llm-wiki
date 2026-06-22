---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.hint.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Bulk.find.hint() (mongosh method)

.. include:: /includes/fact-bulkwrite.rst

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

Create an example collection `orders`:

```javascript
db.orders.insertMany( [
   { "_id" : 1, "item" : "abc", "price" : Decimal128("12"), "quantity" : 2, "type": "apparel" },
   { "_id" : 2, "item" : "jkl", "price" : Decimal128("20"), "quantity" : 1, "type": "electronics" },
   { "_id" : 3, "item" : "abc", "price" : Decimal128("10"), "quantity" : 5, "type": "apparel" },
   { "_id" : 4, "item" : "abc", "price" : Decimal128("8"), "quantity" : 10, "type": "apparel" },
   { "_id" : 5, "item" : "jkl", "price" : Decimal128("15"), "quantity" : 15, "type": "electronics" }
] )
```

Create the following indexes on the example collection:

```javascript
db.orders.createIndex( { item: 1 } );
db.orders.createIndex( { item: 1, quantity: 1 } );
db.orders.createIndex( { item: 1, price: 1 } );
```

The following bulk operations specify different index to use for the various update/replace document operations:

```javascript
var bulk = db.orders.initializeUnorderedBulkOp();
bulk.find({ item: "abc", price: { $gte: Decimal128("10") }, quantity: { $lte: 10 } }).hint({item: 1, quantity: 1}).replaceOne( { item: "abc123", status: "P", points: 100 } );
bulk.find({ item: "abc", price: { $gte: Decimal128("10") }, quantity: { $lte: 10 } }).hint({item: 1, price: 1}).updateOne( { $inc: { points: 10 } } );
bulk.execute();
```

To view the indexes used, you can use the :pipeline:`$indexStats` pipeline:

```javascript
db.orders.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } } ] )
```

> **Seealso:** - :method:`db.collection.initializeUnorderedBulkOp()`
- :method:`db.collection.initializeOrderedBulkOp()`
- :method:`Bulk.find()`
- :method:`Bulk.execute()`
- `All Bulk Methods <bulk-methods>`
