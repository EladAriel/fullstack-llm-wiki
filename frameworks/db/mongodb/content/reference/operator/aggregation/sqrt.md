---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/sqrt.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $sqrt (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-double-unless-decimal-behavior.rst

.. include:: /includes/extracts/agg-expression-null-operand-sqrt.rst

:expression:`$sqrt` errors on negative numbers.

## Example

A collection `points` contains the following documents:

```javascript
db.points.insertMany( [ 
   { _id: 1, p1: { x: 5, y: 8 }, p2: { x: 0, y: 5} },
   { _id: 2, p1: { x: -2, y: 1 }, p2: { x: 1, y: 5} },
   { _id: 3, p1: { x: 4, y: 4 }, p2: { x: 4, y: 0} }
] )
```

The following example uses :expression:`$sqrt` to calculate the distance between `p1` and `p2`:

```javascript
db.points.aggregate([
   {
     $project: {
        distance: {
           $sqrt: { 
               $add: [
                  { $pow: [ { $subtract: [ "$p2.y", "$p1.y" ] }, 2 ] },
                  { $pow: [ { $subtract: [ "$p2.x", "$p1.x" ] }, 2 ] }
               ]
           }
        }
     }
   }
])
```

The operation returns the following results:

```javascript
{ _id: 1, distance: 5.830951894845301 }
{ _id: 2, distance: 5 }
{ _id: 3, distance: 4 }
```
