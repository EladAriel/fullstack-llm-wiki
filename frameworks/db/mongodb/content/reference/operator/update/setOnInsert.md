---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/setOnInsert.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# $setOnInsert (update operator)

## Definition

## Behavior

.. include:: /includes/fact-update-operator-processing-order.rst

.. include:: /includes/extracts/update-operation-empty-operand-expressions-set-on-insert.rst

## Example

The `products` collection contains no documents.

Insert a new document using :method:`db.collection.updateOne()` the `upsert: true <upsert-parameter>` parameter.

```javascript
db.products.updateOne(
  { _id: 1 },
  {
     $set: { item: "apple" },
     $setOnInsert: { defaultQty: 100 }
  },
  { upsert: true }
)
```

MongoDB uses `<query> to create a new document with id: 1`. :update:`$setOnInsert` updates the document as specified.

The `products` collection contains the newly-inserted document:

```javascript
{ "_id" : 1, "item" : "apple", "defaultQty" : 100 }
```

When the `upsert <upsert-parameter>` parameter is `true` :method:`db.collection.updateOne()`:

- creates a new document
- applies the :update:`$set` operation
- applies the :update:`$setOnInsert` operation
If :method:`db.collection.updateOne()` matches an existing document, MongoDB only applies the :update:`$set` operation.

> **Seealso:** - :method:`db.collection.updateOne()`
- :method:`db.collection.findOneAndUpdate()`
