---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/pow.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# $pow (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-order-of-return-behavior.rst

.. include:: /includes/extracts/agg-expression-null-operand-pow.rst

## Example

Create a collection called `quizzes` with the following documents:

```javascript
db.quizzes.insertMany( [
   { 
      _id : 1, 
      scores : [
         { name : "dave123", score : 85 },
         { name : "dave2", score : 90 },
         { name : "ahn", score : 71 }
      ]
   },
   {
      _id : 2,
      scores : [
         { name : "li", quiz : 2, score : 96 },
         { name : "annT", score : 77 },
         { name : "ty", score : 82 }
      ]
   }
] )
```

The following example calculates the variance for each quiz:

```javascript
db.quizzes.aggregate( [
   { $project: { variance: { $pow: [ { $stdDevPop: "$scores.score" }, 2 ] } } }
] )
```

The operation returns the following results:

```javascript
{ _id : 1, variance : 64.66666666666667 }
{ _id : 2, variance : 64.66666666666667 }
```
