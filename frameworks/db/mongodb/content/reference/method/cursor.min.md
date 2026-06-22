---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.min.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# cursor.min() (mongosh method)

## Definition

.. include:: /includes/cursor-index-use

> **Seealso:** :method:`~cursor.max()`

:method:`~cursor.min()` exists primarily to support the :binary:`~bin.mongos` process.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behaviors

### Interaction with Index Selection

Because :method:`~cursor.min()` requires an index on a field, and forces the query to use this index, you may prefer the :query:`$gte` operator for the query if possible. Consider the following example:

```javascript
db.products.find( { _id: { $in: [ 6, 7 ] } } ).min( { price: Decimal128("1.39") } ).hint( { price: 1 } )
```

The query will use the index on the `price field, even if the index on id` may be better.

### Index Bounds

If you use :method:`~cursor.min()` with :method:`~cursor.max()` to specify a range:

- the index bounds specified in :method:`~cursor.min()` and
:method:`~cursor.max()` must both refer to the keys of the same index.

- the bound specified by :method:`~cursor.max()` must be greater than
the bound specified by :method:`~cursor.min()`.

### `min()` without `max()`

.. include:: /includes/fact-query-min-max.rst

## Example

Unless the :method:`~db.collection.find() query is an equality condition on the id` field `{ _id: <value> }`, you must explicitly specify the index with the :method:`~cursor.hint()` method to run :method:`~cursor.min()`.

For the examples below, create a sample collection named `products` that holds the following documents:

```javascript
db.products.insertMany([
   { "_id" : 1, "item" : "apple", "type" : "honey crisp", "price" : Decimal128("1.99") },
   { "_id" : 2, "item" : "apple", "type" : "fuji", "price" : Decimal128("1.99") },
   { "_id" : 3, "item" : "apple", "type" : "jonagold", "price" : Decimal128("1.29") },
   { "_id" : 4, "item" : "apple", "type" : "jonathan", "price" : Decimal128("1.29") },
   { "_id" : 5, "item" : "apple", "type" : "mcintosh", "price" : Decimal128("1.29") },
   { "_id" : 6, "item" : "apple", "type" : "cortland", "price" : Decimal128("1.29") },
   { "_id" : 7, "item" : "orange", "type" : "cara cara", "price" : Decimal128("2.99") },
   { "_id" : 9, "item" : "orange", "type" : "satsuma", "price" : Decimal128("1.99") },
   { "_id" : 8, "item" : "orange", "type" : "valencia", "price" : Decimal128("0.99") },
   { "_id" : 10, "item" : "orange", "type" : "navel", "price" : Decimal128("1.39") }
])
```

Create the following indexes for the collection:

```javascript
db.products.createIndexes( [
   { "item" : 1, "type" : 1 },
   { "item" : 1, "type" : -1 },
   { "price" : 1 } 
] )
```

- Using the ordering of the `{ item: 1, type: 1 }` index,
:method:`~cursor.min()` limits the query to the documents that are at or above the index key bound of `item` equal to `apple` and `type` equal to `jonagold`, as in the following:

```javascript
  db.products.find().min( { item: 'apple', type: 'jonagold' } ).hint( { item: 1, type: 1 } )

The query returns the following documents:

.. code-block:: javascript

  { "_id" : 3, "item" : "apple", "type" : "jonagold", "price" : Decimal128("1.29") }
  { "_id" : 4, "item" : "apple", "type" : "jonathan", "price" : Decimal128("1.29") }
  { "_id" : 5, "item" : "apple", "type" : "mcintosh", "price" : Decimal128("1.29") }
  { "_id" : 7, "item" : "orange", "type" : "cara cara", "price" : Decimal128("2.99") }
  { "_id" : 10, "item" : "orange", "type" : "navel", "price" : Decimal128("1.39") }
  { "_id" : 9, "item" : "orange", "type" : "satsuma", "price" : Decimal128("1.99") }
  { "_id" : 8, "item" : "orange", "type" : "valencia", "price" : Decimal128("0.99") }
```

- Using the ordering of the index `{ price: 1 }`, :method:`~cursor.min()` limits the query to the documents that are at or
above the index key bound of `price` equal to `1.39` and :method:`~cursor.max()` limits the query to the documents that are below the index key bound of `price` equal to `1.99`:

> **Note:**   The bound specified by :method:`~cursor.max()` must be greater than the
  bound specified by :method:`~cursor.min()`.
.. code-block:: javascript
   db.products.find().min( { price: Decimal128("1.39") } ).max( { price:  Decimal128("1.99") } ).hint( { price: 1 } )
The query returns the following documents:
.. code-block:: javascript
  { "_id" : 10, "item" : "orange", "type" : "navel", "price" : Decimal128("1.39") }
