---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/and.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# $and (expression operator)

## Definition

## Behavior

.. include:: /includes/extracts/fact-agg-boolean-and.rst

## Error Handling

.. include:: /includes/and-or-behavior.rst

## Example

Create an example `inventory` collection with these documents:

```javascript
db.inventory.insertMany([
   { _id: 1, item: "abc1", description: "product 1", qty: 300 },
   { _id: 2, item: "abc2", description: "product 2", qty: 200 },
   { _id: 3, item: "xyz1", description: "product 3", qty: 250 },
   { _id: 4, item: "VWZ1", description: "product 4", qty: 300 },
   { _id: 5, item: "VWZ2", description: "product 5", qty: 180 }
])
```

This operation uses the :expression:`$and` operator to determine if `qty` is greater than 100 and less than `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            result: { $and: [ { $gt: [ "$qty", 100 ] }, { $lt: [ "$qty", 250 ] } ] }
          }
     }
   ]
)
```

The operation returns these results:

```javascript
{ _id: 1, item: "abc1", qty: 300, result: false }
{ _id: 2, item: "abc2", qty: 200, result: true }
{ _id: 3, item: "xyz1", qty: 250, result: false }
{ _id: 4, item: "VWZ1", qty: 300, result: false }
{ _id: 5, item: "VWZ2", qty: 180, result: true }
```
