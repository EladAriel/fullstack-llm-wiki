---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/gt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $gt (expression operator)

## Definition

## Example

Create an `inventory` collection with these documents:

.. include:: /includes/examples-create-inventory-2.rst

Use the `$gt` operator to determine if `qty` is greater than `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            qtyGt250: { $gt: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ item : "abc1", qty : 300, qtyGt250 : true }
{ item : "abc2", qty : 200, qtyGt250 : false }
{ item : "xyz1", qty : 250, qtyGt250 : false }
{ item : "VWZ1", qty : 300, qtyGt250 : true }
{ item : "VWZ2", qty : 180, qtyGt250 : false }
```
