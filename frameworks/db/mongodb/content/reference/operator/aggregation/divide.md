---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/divide.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# $divide (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-double-unless-decimal-behavior.rst

## Examples

Consider a `conferencePlanning` collection with the following documents:

```javascript
db.conferencePlanning.insertMany( [
   { "_id" : 1, "city" : "New York", "hours" : 80, "tasks" : 7 },
   { "_id" : 2, "city" : "Singapore", "hours" : 40, "tasks" : 4 }
] )
```

The following aggregation uses the :expression:`$divide` expression to divide the `hours` field by a literal `8` to compute the number of work days:

```javascript
db.planning.aggregate(
   [
     { $project: { city: 1, workdays: { $divide: [ "$hours", 8 ] } } }
   ]
)
```

The operation returns the following results:

```javascript
{ "_id" : 1, "city" : "New York", "workdays" : 10 }
{ "_id" : 2, "city" : "Singapore", "workdays" : 5 }
```
