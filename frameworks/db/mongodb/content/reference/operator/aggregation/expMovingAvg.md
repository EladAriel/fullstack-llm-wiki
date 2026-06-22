---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/expMovingAvg.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# $expMovingAvg (expression operator)

## Definition

.. versionadded:: 5.0

Returns the exponential moving average of numeric `expressions <aggregation-expressions>` applied to documents in a `partition <setWindowFields-partitionBy>` defined in the :pipeline:`$setWindowFields` stage.

:group:`$expMovingAvg` is only available in the :pipeline:`$setWindowFields` stage.

:group:`$expMovingAvg` syntax:

```none
{
   $expMovingAvg: {
      input: <input expression>,
      N: <integer>,
      alpha: <float>
   }
} 
```

:group:`$expMovingAvg` takes a document with these fields:

## Behavior

.. include:: /includes/expMovingAvg-N-or-alpha.rst

:group:`$expMovingAvg` ignores non-numeric values, `null` values, and missing fields.

## Examples

Create a `stockPrices` collection that contains prices for stocks named `"MDB"` and `"MSFT"`:

```javascript
db.stockPrices.insertMany( [
   { stock: "MDB", date: new Date( "2020-05-18T20:00:00Z" ), price: 13 },
   { stock: "MDB", date: new Date( "2020-05-19T20:00:00Z" ), price: 15.4 },
   { stock: "MDB", date: new Date( "2020-05-20T20:00:00Z" ), price: 12 },
   { stock: "MDB", date: new Date( "2020-05-21T20:00:00Z" ), price: 11.7 },
   { stock: "MSFT", date: new Date( "2020-05-18T20:00:00Z" ), price: 82 },
   { stock: "MSFT", date: new Date( "2020-05-19T20:00:00Z" ), price: 94 },
   { stock: "MSFT", date: new Date( "2020-05-20T20:00:00Z" ), price: 112 },
   { stock: "MSFT", date: new Date( "2020-05-21T20:00:00Z" ), price: 97.3 }
] )
```

### Exponential Moving Average Using `N`

This example uses :group:`$expMovingAvg` in the :pipeline:`$setWindowFields` stage to output the exponential moving average for the stock prices weighted for two historical documents (two days for the example documents) using `N <expMovingAvg-N>` set to `2`:

```javascript
db.stockPrices.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$stock",
         sortBy: { date: 1 },
         output: {
            expMovingAvgForStock: {
               $expMovingAvg: { input: "$price", N: 2 }
            }
         }
      }
   }
] )
```

In the example:

- `partitionBy: "$stock"` :ref:`partitions
<setWindowFields-partitionBy>` the documents in the collection by `stock`. There are partitions for `"MDB"` and `"MSFT"`.

- `sortBy: { date: 1 }` :ref:`sorts
<setWindowFields-sortBy>` the documents in each partition by `date` in ascending order (`1`), so the earliest `date` is first.

- `output` returns the exponential moving average for the stock
`price` field with `N <expMovingAvg-N>` set to `2`:

- In the input documents, there is one document for each day
and the documents are ordered by `date`. Therefore, with `N <expMovingAvg-N>` is set to `2`, the `price` in the current document and the `price` in the previous document, if available, are allocated the highest weight in the `exponential moving average formula <expMovingAvg-N>`.

- The exponential moving average for the `price` field is stored in
a new field called `expMovingAvgForStocks`, as shown in the following results.

```javascript
{ "_id" : ObjectId("60d11fef833dfeadc8e6286b"), "stock" : "MDB",
  "date" : ISODate("2020-05-18T20:00:00Z"), "price" : 13,
  "expMovingAvgForStock" : 13 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286c"), "stock" : "MDB",
  "date" : ISODate("2020-05-19T20:00:00Z"), "price" : 15.4,
  "expMovingAvgForStock" : 14.6 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286d"), "stock" : "MDB",
  "date" : ISODate("2020-05-20T20:00:00Z"), "price" : 12,
  "expMovingAvgForStock" : 12.866666666666667 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286e"), "stock" : "MDB",
  "date" : ISODate("2020-05-21T20:00:00Z"), "price" : 11.7,
  "expMovingAvgForStock" : 12.088888888888889 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286f"), "stock" : "MSFT",
  "date" : ISODate("2020-05-18T20:00:00Z"), "price" : 82,
  "expMovingAvgForStock" : 82 }
{ "_id" : ObjectId("60d11fef833dfeadc8e62870"), "stock" : "MSFT",
  "date" : ISODate("2020-05-19T20:00:00Z"), "price" : 94,
  "expMovingAvgForStock" : 90 }
{ "_id" : ObjectId("60d11fef833dfeadc8e62871"), "stock" : "MSFT",
  "date" : ISODate("2020-05-20T20:00:00Z"), "price" : 112,
  "expMovingAvgForStock" : 104.66666666666667 }
{ "_id" : ObjectId("60d11fef833dfeadc8e62872"), "stock" : "MSFT",
  "date" : ISODate("2020-05-21T20:00:00Z"), "price" : 97.3,
  "expMovingAvgForStock" : 99.75555555555556 }
```

### Exponential Moving Average Using `alpha`

This example uses :group:`$expMovingAvg` in the :pipeline:`$setWindowFields` stage to output the exponential moving average for the stock prices using `alpha <expMovingAvg-alpha>` set to `0.75`:

```javascript
db.stockPrices.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$stock",
         sortBy: { date: 1 },
         output: {
            expMovingAvgForStock: {
               $expMovingAvg: { input: "$price", alpha: 0.75 }
            }
         }
      }
   }
] )
```

In the example:

- `partitionBy: "$stock"` :ref:`partitions
<setWindowFields-partitionBy>` the documents in the collection by `stock`. There are partitions for `"MDB"` and `"MSFT"`.

- `sortBy: { date: 1 }` :ref:`sorts
<setWindowFields-sortBy>` the documents in each partition by `date` in ascending order (`1`), so the earliest `date` is first.

- `output` sets the exponential moving average for the stock prices in
a new field called `expMovingAvgForStock`, as shown in the following results. The value for `alpha <expMovingAvg-alpha>` is set to `0.75` in the `exponential moving average formula <expMovingAvg-alpha>`.

```javascript
{ "_id" : ObjectId("60d11fef833dfeadc8e6286b"), "stock" : "MDB",
  "date" : ISODate("2020-05-18T20:00:00Z"), "price" : 13,
  "expMovingAvgForStock" : 13 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286c"), "stock" : "MDB",
  "date" : ISODate("2020-05-19T20:00:00Z"), "price" : 15.4,
  "expMovingAvgForStock" : 14.8 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286d"), "stock" : "MDB",
  "date" : ISODate("2020-05-20T20:00:00Z"), "price" : 12,
  "expMovingAvgForStock" : 12.7 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286e"), "stock" : "MDB",
  "date" : ISODate("2020-05-21T20:00:00Z"), "price" : 11.7,
  "expMovingAvgForStock" : 11.95 }
{ "_id" : ObjectId("60d11fef833dfeadc8e6286f"), "stock" : "MSFT",
  "date" : ISODate("2020-05-18T20:00:00Z"), "price" : 82,
  "expMovingAvgForStock" : 82 }
{ "_id" : ObjectId("60d11fef833dfeadc8e62870"), "stock" : "MSFT",
  "date" : ISODate("2020-05-19T20:00:00Z"), "price" : 94,
  "expMovingAvgForStock" : 91 }
{ "_id" : ObjectId("60d11fef833dfeadc8e62871"), "stock" : "MSFT",
  "date" : ISODate("2020-05-20T20:00:00Z"), "price" : 112,
  "expMovingAvgForStock" : 106.75 }
{ "_id" : ObjectId("60d11fef833dfeadc8e62872"), "stock" : "MSFT",
  "date" : ISODate("2020-05-21T20:00:00Z"), "price" : 97.3,
  "expMovingAvgForStock" : 99.6625 }
```
