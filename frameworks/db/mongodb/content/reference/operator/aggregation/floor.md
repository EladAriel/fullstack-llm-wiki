---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/floor.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $floor (expression operator)

## Definition

## Behavior

.. include:: /includes/extracts/agg-expression-null-operand-floor.rst

## Example

Create a collection named `samples` with the following documents:

```javascript
db.samples.insertMany(
   [
      { _id: 1, value: 9.25 },
      { _id: 2, value: 8.73 },
      { _id: 3, value: 4.32 },
      { _id: 4, value: -5.34 }
   ]
)
```

The following example returns both the original value and the floor value:

```javascript
db.samples.aggregate([
   { $project: { value: 1, floorValue: { $floor: "$value" } } }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "value" : 9.25, "floorValue" : 9 }
{ "_id" : 2, "value" : 8.73, "floorValue" : 8 }
{ "_id" : 3, "value" : 4.32, "floorValue" : 4 }
{ "_id" : 4, "value" : -5.34, "floorValue" : -6 }
```
