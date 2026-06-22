---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/covariancePop.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# $covariancePop (expression operator)

## Definition

.. versionadded:: 5.0

Returns the population covariance of two numeric `expressions <aggregation-expressions>` that are evaluated using documents in the :pipeline:`$setWindowFields` stage `window <setWindowFields-window>`.

:group:`$covariancePop` is only available in the :pipeline:`$setWindowFields` stage.

:group:`$covariancePop` syntax:

```none
{
   $covariancePop: 
   [
      <numeric expression 1>,
      <numeric expression 2>
   ]
} 
```

## Behavior

:group:`$covariancePop` behavior:

.. include:: /includes/covariance-behavior.rst

## Example

.. include:: /includes/setWindowFields-example-collection.rst

This example uses :group:`$covariancePop` in the :pipeline:`$setWindowFields` stage to output the population covariance values for the cake sales `orderDate` year and `quantity` values:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { orderDate: 1 },
         output: {
            covariancePopForState: {
               $covariancePop: [ { $year: "$orderDate" }, "$quantity" ],
               window: {
                  documents: [ "unbounded", "current" ]
               }
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-date.rst

- `output` sets the population covariance values for the
`orderDate` year and `quantity` values using :group:`$covariancePop` run in a `documents <setWindowFields-documents>` window.

The `window <setWindowFields-window>` contains documents between an `unbounded` lower limit and the `current` document in the output. This means :group:`$covariancePop` sets the `covariancePopForState` field to the population covariance values for the documents between the beginning of the partition and the current document.

In this output, the population covariance is shown in the `covariancePopForState` field:

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "covariancePopForState" : 0 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "covariancePopForState" : -10.5 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "covariancePopForState" : -5.666666666666671 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "covariancePopForState" : 0 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "covariancePopForState" : -7.5 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "covariancePopForState" : 2 }
```
