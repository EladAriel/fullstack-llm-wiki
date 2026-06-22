---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/log10.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $log10 (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-double-unless-decimal-behavior.rst

.. include:: /includes/extracts/agg-expression-null-operand-log10.rst

## Example

Create a collection named `samples` with the following documents:

```javascript
db.samples.insertMany(
   [
      { _id: 1, H3O: 0.0025 },
      { _id: 2, H3O: 0.001 },
      { _id: 3, H3O: 0.02 }
   ]
)
```

The following example calculates the pH value of the samples:

```javascript
db.samples.aggregate( [ 
   { $project: { pH: { $multiply: [ -1, { $log10: "$H3O" } ] } } }
] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "pH" : 2.6020599913279625 }
{ "_id" : 2, "pH" : 3 }
{ "_id" : 3, "pH" : 1.6989700043360187 }
```

> **Seealso:** :expression:`$log`
