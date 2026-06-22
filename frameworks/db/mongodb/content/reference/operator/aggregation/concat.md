---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/concat.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $concat (expression operator)

## Definition

## Example

Create an `inventory` collection with these documents:

```javascript
db.inventory.insertMany( [
   { _id : 1, item : "ABC1", quarter: "13Q1", description : "product 1" },
   { _id : 2, item : "ABC2", quarter: "13Q4", description : "product 2" },
   { _id : 3, item : "XYZ1", quarter: "14Q2", description : null }
] )
```

Use the `$concat` operator to concatenate the `item` field and the `description` field with a " - " delimiter:

```javascript
db.inventory.aggregate(
   [
      { $project: { itemDescription: { $concat: [ "$item", " - ", "$description" ] } } }
   ]
)
```

Output:

```javascript
{ _id : 1, itemDescription : "ABC1 - product 1" }
{ _id : 2, itemDescription : "ABC2 - product 2" }
{ _id : 3, itemDescription : null }
```
