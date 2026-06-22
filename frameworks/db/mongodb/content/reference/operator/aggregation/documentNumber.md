---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/documentNumber.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# $documentNumber (expression operator)

## Definition

.. versionadded:: 5.0

Returns the position of a document (known as the document number) in the :pipeline:`$setWindowFields` stage `partition <setWindowFields-partitionBy>`.

The :pipeline:`$setWindowFields` stage `sortBy <setWindowFields-sortBy>` field determines the document number. For more information on how MongoDB compares fields with different types, see `BSON comparison order <bson-types-comparison-order>`.

:group:`$documentNumber` returns a unique number for each document in a `partition <setWindowFields-partitionBy>`, even if multiple documents have identical `sortBy <setWindowFields-sortBy>` field values in the `partition <setWindowFields-partitionBy>`.

:group:`$documentNumber` is only available in the :pipeline:`$setWindowFields` stage.

:group:`$documentNumber` syntax:

```none
{ $documentNumber: { } }
```

:group:`$documentNumber` does not accept any parameters.

## Behavior

:group:`$documentNumber` includes documents that have a `sortBy <setWindowFields-sortBy>` field that is `null` or missing.

:group:`$documentNumber`, :group:`$rank`, and :group:`$denseRank` return the position of the documents based on the `sortBy <setWindowFields-sortBy>` field values.

:group:`$documentNumber` differs from :group:`$rank` and :group:`$denseRank` in how documents with identical `sortBy <setWindowFields-sortBy>` field values in a `partition <setWindowFields-partitionBy>` are treated:

- :group:`$rank` and :group:`$denseRank` return the same position (known
as the rank) for those documents.

- :group:`$documentNumber` returns a unique position (known as the
document number) for those documents.

See the example in `documentNumber-duplicate-null-missing-values-example`.

## Examples

### Document Number for Each State

.. include:: /includes/setWindowFields-example-collection.rst

This example uses :group:`$documentNumber` in the :pipeline:`$setWindowFields` stage to output the cake sales document number for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { quantity: -1 },
         output: {
            documentNumberForState: {
               $documentNumber: {}  
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-quantity.rst

- `output` sets the document number in a new field called
`documentNumberForState` shown in the following results. `documentNumberForState` is unique within each `state` partition.

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "documentNumberForState" : 1 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "documentNumberForState" : 2 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "documentNumberForState" : 3 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "documentNumberForState" : 1 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "documentNumberForState" : 2 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "documentNumberForState" : 3 }
```

### Document Number for Duplicate, Null, and Missing Values

.. include:: /includes/setWindowFields-duplicates-example-collection.rst

This example uses :group:`$documentNumber` in the :pipeline:`$setWindowFields` stage to output the `cakeSalesWithDuplicates` document number for each `state`:

```javascript
db.cakeSalesWithDuplicates.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { quantity: -1 },
         output: {
            documentNumberForState: {
               $documentNumber: {}  
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-quantity.rst

- `output` sets the document number in a new field called
`documentNumberForState` shown in the following results. `documentNumberForState` is unique within each `state` partition, and there are `documentNumberForState` values for documents with `null` `quantity` and missing `quantity` values.

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "documentNumberForState" : 1 }
{ "_id" : 9, "type" : "strawberry", "orderDate" : ISODate("2020-05-11T16:09:01Z"),
  "state" : "CA", "price" : 39, "quantity" : 162, "documentNumberForState" : 2 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "documentNumberForState" : 3 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "documentNumberForState" : 4 }
{ "_id" : 10, "type" : "strawberry", "orderDate" : ISODate("2020-05-11T16:09:01Z"),
  "state" : "CA", "price" : 39, "quantity" : null, "documentNumberForState" : 5 }
{ "_id" : 11, "type" : "strawberry", "orderDate" : ISODate("2020-05-11T16:09:01Z"),
  "state" : "CA", "price" : 39, "documentNumberForState" : 6 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "documentNumberForState" : 1 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "documentNumberForState" : 2 }
{ "_id" : 6, "type" : "strawberry", "orderDate" : ISODate("2020-01-08T06:12:03Z"),
  "state" : "WA", "price" : 41, "quantity" : 134, "documentNumberForState" : 3 }
{ "_id" : 7, "type" : "strawberry", "orderDate" : ISODate("2020-01-01T06:12:03Z"),
  "state" : "WA", "price" : 34, "quantity" : 134, "documentNumberForState" : 4 }
{ "_id" : 8, "type" : "strawberry", "orderDate" : ISODate("2020-01-02T06:12:03Z"),
  "state" : "WA", "price" : 40, "quantity" : 134, "documentNumberForState" : 5 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "documentNumberForState" : 6 }
```
