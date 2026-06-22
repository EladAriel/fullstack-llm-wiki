---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/abs.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $abs (expression operator)

## Definition

## Behavior

.. include:: /includes/extracts/agg-expression-null-operand-abs.rst

## Example

A collection `temperatureChange` contains the following documents:

```javascript
db.temperatureChange.insertMany( [
   { _id: 1, startTemp: 50, endTemp: 80 },
   { _id: 2, startTemp: 40, endTemp: 40 },
   { _id: 3, startTemp: 90, endTemp: 70 },
   { _id: 4, startTemp: 60, endTemp: 70 }
] )
```

The following example calculates the magnitude of difference between the `startTemp` and `endTemp` ratings:

```javascript
db.temperatureChange.aggregate([
   {
      $project: { delta: { $abs: { $subtract: [ "$startTemp", "$endTemp" ] } } }
   }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "delta" : 30 }
{ "_id" : 2, "delta" : 0 }
{ "_id" : 3, "delta" : 20 }
{ "_id" : 4, "delta" : 10 }
```
