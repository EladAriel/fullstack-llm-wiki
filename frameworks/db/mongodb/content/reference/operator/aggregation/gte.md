---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/gte.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# $gte (expression operator)

## Definition

## Example

Create an `inventory` collection with these documents:

.. include:: /includes/examples-create-inventory-2.rst

Use the `$gte` operator to determine if `qty` is greater than or equal to `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            qtyGte250: { $gte: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

Output:

```javascript
{ item : "abc1", qty : 300, qtyGte250 : true }
{ item : "abc2", qty : 200, qtyGte250 : false }
{ item : "xyz1", qty : 250, qtyGte250 : true }
{ item : "VWZ1", qty : 300, qtyGte250 : true }
{ item : "VWZ2", qty : 180, qtyGte250 : false }
```
