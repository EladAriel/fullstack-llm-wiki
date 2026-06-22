---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/eq.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $eq (expression operator)

## Definition

## Example

Create an `inventory` collection with these documents:

.. include:: /includes/examples-create-inventory-2.rst

Use the `$eq` operator to determine if `qty` equals `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            qtyEq250: { $eq: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

Output:

```javascript
{ item : "abc1", qty : 300, qtyEq250 : false }
{ item : "abc2", qty : 200, qtyEq250 : false }
{ item : "xyz1", qty : 250, qtyEq250 : true }
{ item : "VWZ1", qty : 300, qtyEq250 : false }
{ item : "VWZ2", qty : 180, qtyEq250 : false }
```
