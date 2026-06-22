---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toLower.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $toLower  (expression operator)

## Definition

## Behavior

.. include:: /includes/intro-aggregation-string.rst

## Example

Consider a `inventory` collection with the following documents:

.. include:: /includes/toLower-toUpper-sample-data.rst

The following operation uses the :expression:`$toLower` operator return lowercase `item` and lowercase `description` value:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
         {
           item: { $toLower: "$item" },
           description: { $toLower: "$description" }
         }
     }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "abc1", description: "product 1" }
{ _id: 2, item: "abc2", description: "product 2" }
{ _id: 3, item: "xyz1", description: "" }
```
