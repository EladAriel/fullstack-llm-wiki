---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/exp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $exp (expression operator)

## Definition

## Behavior

.. include:: /includes/agg-expression-double-unless-decimal-behavior.rst

.. include:: /includes/extracts/agg-expression-null-operand-exp.rst

## Example

A collection named `accounts` contains the following documents:

```javascript
db.accounts.insertMany( [
   { _id: 1, interestRate: .08, presentValue: 10000 },
   { _id: 2, interestRate: .0825, presentValue: 250000 },
   { _id: 3, interestRate: .0425, presentValue: 1000 }
] )
```

The following example calculates the effective interest rate for continuous compounding:

```javascript
db.accounts.aggregate( [ { $project: { effectiveRate: { $subtract: [ { $exp: "$interestRate"}, 1 ] } } } ] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "effectiveRate" : 0.08328706767495864 }
{ "_id" : 2, "effectiveRate" : 0.08599867343905654 }
{ "_id" : 3, "effectiveRate" : 0.04341605637367807 }
```
