---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/denseRank.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $denseRank (expression operator)

## Definition

.. versionadded:: 5.0

Returns the document position (known as the rank) relative to other documents in the :pipeline:`$setWindowFields` stage `partition <setWindowFields-partitionBy>`.

The :pipeline:`$setWindowFields` stage `sortBy <setWindowFields-sortBy>` field value determines the document rank. For more information on how MongoDB compares fields with different types, see `BSON comparison order <bson-types-comparison-order>`.

If multiple documents occupy the same rank, :group:`$denseRank` places the document with the subsequent value at the next rank without any gaps (see `denseRank-behavior`).

:group:`$denseRank` is only available in the :pipeline:`$setWindowFields` stage.

:group:`$denseRank` syntax:

```none
{ $denseRank: { } }
```

:group:`$denseRank` does not accept any parameters.

> **Seealso:** :group:`$rank`

## Behavior

.. include:: /includes/rank-and-denseRank-behavior.rst

See the example in `denseRank-duplicate-null-missing-values-example`.

## Examples

### Dense Rank Partitions by an Integer Field

.. include:: /includes/setWindowFields-example-collection.rst

This example uses :group:`$denseRank` in the :pipeline:`$setWindowFields` stage to output the `quantity` dense rank of the cake sales for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { quantity: -1 },
         output: {
            denseRankQuantityForState: {
               $denseRank: {}  
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-quantity.rst

- `output` sets the `denseRankOrderDateForState` field to the
`orderDate` dense rank using :group:`$denseRank`, as shown in the following results.

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "denseRankQuantityForState" : 1 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "denseRankQuantityForState" : 2 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "denseRankQuantityForState" : 3 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "denseRankQuantityForState" : 1 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "denseRankQuantityForState" : 2 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "denseRankQuantityForState" : 3 }
```

### Dense Rank Partitions by a Date Field

This example shows how to use dates with :group:`$denseRank` in the :pipeline:`$setWindowFields` stage to output the `orderDate` dense rank of the cake sales for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { orderDate: 1 },
         output: {
            denseRankOrderDateForState: {
               $denseRank: {}
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-date.rst

- `output` sets the `denseRankOrderDateForState` field to the
`orderDate` rank using :group:`$denseRank`, as shown in the following results.

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "denseRankOrderDateForState" : 1 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "denseRankOrderDateForState" : 2 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "denseRankOrderDateForState" : 3 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "denseRankOrderDateForState" : 1 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "denseRankOrderDateForState" : 2 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "denseRankOrderDateForState" : 3 }
```

### Dense Rank for Duplicate, Null, and Missing Values

.. include:: /includes/setWindowFields-duplicates-example-collection.rst

This example uses :group:`$denseRank` in the :pipeline:`$setWindowFields` stage to output the `quantity` dense rank from the `cakeSalesWithDuplicates` collection for each `state`:

```javascript
db.cakeSalesWithDuplicates.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { quantity: -1 },
         output: {
            denseRankQuantityForState: {
               $denseRank: {}  
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-quantity.rst

- `output` sets the `denseRankQuantityForState` field to the
`quantity` dense rank using :group:`$denseRank`.

In the following example output:

- The documents with the same `quantity` and `state` have the same
rank and there is no gap between the ranks. This differs from :group:`$rank` that has a gap between the ranks (for an example, see `rank-duplicate-null-missing-values-example`).

- The document with the `null` `quantity` and then the document with
the missing `quantity` are ranked the lowest in the output for the `CA` partition. This sorting is the result of the `BSON comparison order <bson-types-comparison-order>`, which sorts `null` and missing values after number values in this example.

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "denseRankQuantityForState" : 1 }
{ "_id" : 9, "type" : "strawberry", "orderDate" : ISODate("2020-05-11T16:09:01Z"),
  "state" : "CA", "price" : 39, "quantity" : 162, "denseRankQuantityForState" : 1 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "denseRankQuantityForState" : 2 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "denseRankQuantityForState" : 3 }
{ "_id" : 10, "type" : "strawberry", "orderDate" : ISODate("2020-05-11T16:09:01Z"),
  "state" : "CA", "price" : 39, "quantity" : null, "denseRankQuantityForState" : 4 }
{ "_id" : 11, "type" : "strawberry", "orderDate" : ISODate("2020-05-11T16:09:01Z"),
  "state" : "CA", "price" : 39, "denseRankQuantityForState" : 5 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "denseRankQuantityForState" : 1 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "denseRankQuantityForState" : 2 }
{ "_id" : 6, "type" : "strawberry", "orderDate" : ISODate("2020-01-08T06:12:03Z"),
  "state" : "WA", "price" : 41, "quantity" : 134, "denseRankQuantityForState" : 2 }
{ "_id" : 7, "type" : "strawberry", "orderDate" : ISODate("2020-01-01T06:12:03Z"),
  "state" : "WA", "price" : 34, "quantity" : 134, "denseRankQuantityForState" : 2 }
{ "_id" : 8, "type" : "strawberry", "orderDate" : ISODate("2020-01-02T06:12:03Z"),
  "state" : "WA", "price" : 40, "quantity" : 134, "denseRankQuantityForState" : 2 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "denseRankQuantityForState" : 3 }
```
