---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/or.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $or (expression operator)

## Definition

## Behavior

.. include:: /includes/extracts/fact-agg-boolean-or.rst

## Error Handling

.. include:: /includes/and-or-behavior.rst

## Example

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "abc1", description: "product 1", qty: 300 },
   { _id: 2, item: "abc2", description: "product 2", qty: 200 },
   { _id: 3, item: "xyz1", description: "product 3", qty: 250 },
   { _id: 4, item: "VWZ1", description: "product 4", qty: 300 },
   { _id: 5, item: "VWZ2", description: "product 5", qty: 180 }
] )
```

The following operation uses the :expression:`$or` operator to determine if `qty` is greater than 250 or less than `200`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            result: { $or: [ { $gt: [ "$qty", 250 ] }, { $lt: [ "$qty", 200 ] } ] }
          }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "abc1", result: true }
{ _id: 2, item: "abc2", result: false }
{ _id: 3, item: "xyz1", result: false }
{ _id: 4, item: "VWZ1", result: true }
{ _id: 5, item: "VWZ2", result: true }
```
