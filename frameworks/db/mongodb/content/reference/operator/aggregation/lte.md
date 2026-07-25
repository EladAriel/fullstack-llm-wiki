---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/lte.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# $lte (expression operator)

## Definition

## Example

Consider an `inventory` collection with the following documents:

.. include:: /includes/lt-lte-sample-data.rst

The following operation uses the :expression:`$lte` operator to determine if `qty` is less than or equal to `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            qtyLte250: { $lte: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ "item" : "abc1", "qty" : 300, "qtyLte250" : false }
{ "item" : "abc2", "qty" : 200, "qtyLte250" : true }
{ "item" : "xyz1", "qty" : 250, "qtyLte250" : true }
{ "item" : "VWZ1", "qty" : 300, "qtyLte250" : false }
{ "item" : "VWZ2", "qty" : 180, "qtyLte250" : true }
```
