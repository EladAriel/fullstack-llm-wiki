---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/ln.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $ln (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-double-unless-decimal-behavior.rst

.. include:: /includes/extracts/agg-expression-null-operand-ln.rst

## Example

A collection `sales` contains the following documents:

```javascript
db.sales.insertMany( [
   { _id: 1, year: "2000", sales: 8700000 },
   { _id: 2, year: "2005", sales: 5000000 },
   { _id: 3, year: "2010", sales: 6250000 }
] )
```

The following example transforms the `sales` data:

```javascript
db.sales.aggregate( [ { $project: { x: "$year", y: { $ln: "$sales"  } } } ] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "x" : "2000", "y" : 15.978833583624812 }
{ "_id" : 2, "x" : "2005", "y" : 15.424948470398375 }
{ "_id" : 3, "x" : "2010", "y" : 15.648092021712584 }
```

> **Seealso:** :expression:`$log`
