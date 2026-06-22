---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/count-accumulator.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $count (accumulator operator)

## Definition

.. versionadded:: 5.0

Returns the number of documents in a group.

.. include:: /includes/extracts/fact-aggregation-accumulator-count.rst

> **Note:** This page describes the :group:`$count` aggregation accumulator. For
the :pipeline:`$count` aggregation pipeline stage, see
:pipeline:`$count (aggregation pipeline) <$count>`.

## Syntax

:group:`$count` syntax:

```none
{ $count: { } }
```

:group:`$count` does not accept any parameters.

## Behavior

:group:`$count` is functionally equivalent to using `{ $sum : 1 }` within the :pipeline:`$group` stage.

> **Seealso:** :group:`$sum`

## Examples

.. include:: /includes/setWindowFields-example-collection.rst

The `cakeSales` collection is used in the following examples.

### Use in `$group` Stage

This example uses :group:`$count` in the :pipeline:`$group` stage to count the number of documents in the `cakeSales` collection for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $group: {
         _id: "$state",
         countNumberOfDocumentsForState: {
            $count: {}
         }
      }
   }
] )
```

In the example:

- `_id: "$state"` groups the documents by the `state` field value.
There are groups for `CA` and `WA`.

- `$count: {}` sets the `countNumberOfDocumentsForState` field to
the number of documents that share the same `state` field value.

In this output, the number of documents for `CA` and `WA` is shown in the `countNumberOfDocumentsForState` field:

```javascript
{ "_id" : "CA", "countNumberOfDocumentsForState" : 3 }
{ "_id" : "WA", "countNumberOfDocumentsForState" : 3 }
```

### Use in `$setWindowFields` Stage

This example uses :group:`$count` in the :pipeline:`$setWindowFields` stage to count the number of documents in the `cakeSales` collection for each `state` defined in the `window <setWindowFields-window>`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { orderDate: 1 },
         output: {
            countNumberOfDocumentsForState: {
               $count: {},
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

- `output` sets the `countNumberOfDocumentsForState` field to the
number of documents using :group:`$count` that is run in a `documents <setWindowFields-documents>` window.

The `window <setWindowFields-window>` contains documents between an `unbounded` lower limit and the `current` document in the output. This means :group:`$count` returns the number of documents between the beginning of the partition and the current document.

In this output, the number of documents for `CA` and `WA` is shown in the `countNumberOfDocumentsForState` field:

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "countNumberOfDocumentsForState" : 1 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "countNumberOfDocumentsForState" : 2 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "countNumberOfDocumentsForState" : 3 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "countNumberOfDocumentsForState" : 1 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "countNumberOfDocumentsForState" : 2 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "countNumberOfDocumentsForState" : 3 }
```
