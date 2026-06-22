---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/lt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $lt (expression operator)

## Definition

## Example

Consider an `inventory` collection with the following documents:

.. include:: /includes/lt-lte-sample-data.rst

The following operation uses the :expression:`$lt` operator to determine if `qty` is less than `250`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            qty: 1,
            qtyLt250: { $lt: [ "$qty", 250 ] },
            _id: 0
          }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ item: "abc1", qty: 300, qtyLt250: false }
{ item: "abc2", qty: 200, qtyLt250: true }
{ item: "xyz1", qty: 250, qtyLt250: false }
{ item: "VWZ1", qty: 300, qtyLt250: false }
{ item: "VWZ2", qty: 180, qtyLt250: true }
```
