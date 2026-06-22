---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toUpper.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $toUpper  (expression operator)

## Definition

## Behavior

.. include:: /includes/intro-aggregation-string.rst

## Example

Consider a `inventory` collection with the following documents:

.. include:: /includes/toLower-toUpper-sample-data.rst

The following operation uses the :expression:`$toUpper` operator to return uppercase `item` and uppercase `description` values:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
         {
           item: { $toUpper: "$item" },
           description: { $toUpper: "$description" }
         }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", description: "PRODUCT 1" }
{ _id: 2, item: "ABC2", description: "PRODUCT 2" }
{ _id: 3, item: "XYZ1", description: "" }
```
