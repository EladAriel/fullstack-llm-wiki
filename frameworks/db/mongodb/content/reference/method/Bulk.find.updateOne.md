---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.updateOne.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# Bulk.find.updateOne() (mongosh method)

.. include:: /includes/fact-bulkwrite.rst

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Behavior

If the `<update>` document contains only `update operator <update-operators>` expressions, as in:

```javascript
{
  $set: { status: "D" },
  $inc: { points: 2 }
}
```

Then, :method:`Bulk.find.updateOne()` updates only the corresponding fields, `status` and `points`, in the document.

## Example

The following example initializes a :method:`Bulk()` operations builder for the `items` collection, and adds various :method:`~Bulk.find.updateOne` operations to the list of operations.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "D" } ).updateOne( { $set: { status: "I", points: "0" } } );
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
bulk.find( {  status: "P" } ).updateOne(
   [  
      { $set: { points: 0, lastModified: "$$NOW" } }
   ]
);
bulk.execute();
```

> **Seealso:** - :method:`db.collection.initializeUnorderedBulkOp()`
- :method:`db.collection.initializeOrderedBulkOp()`
- :method:`Bulk.find()`
- :method:`Bulk.find.update()`
- :method:`Bulk.find.replaceOne()`
- :method:`Bulk.execute()`
- `All Bulk Methods <bulk-methods>`
