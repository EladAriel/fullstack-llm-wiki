---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/shift.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $shift  (expression operator)

## Definition

.. versionadded:: 5.0

Returns the value from an `expression <aggregation-expressions>` applied to a document in a specified position relative to the current document in the :pipeline:`$setWindowFields` stage `partition <setWindowFields-partitionBy>`.

The :pipeline:`$setWindowFields` stage `sortBy <setWindowFields-sortBy>` field value determines the document order. For more information on how MongoDB compares fields with different types, see `BSON comparison order <bson-types-comparison-order>`.

:group:`$shift` is only available in the :pipeline:`$setWindowFields` stage.

:group:`$shift` syntax:

```none
{
   $shift: {
      output: <output expression>, 
      by: <integer>,
      default: <default expression>
   }
}
```

:group:`$shift` takes a document with these fields:

## Behavior

:group:`$shift` returns an error if you specify a `window <setWindowFields-window>` in the :pipeline:`$setWindowFields` stage.

## Examples

.. include:: /includes/setWindowFields-example-collection.rst

The `cakeSales` collection is used in the following examples.

### Shift Using a Positive Integer

This example uses :group:`$shift` in the :pipeline:`$setWindowFields` stage to output the `quantity` of the cake sales from each document following the current document for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { quantity: -1 },
         output: {
            shiftQuantityForState: {
               $shift: {
                  output: "$quantity",
                  by: 1,
                  default: "Not available"
               }
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-quantity.rst

- `output` after `sortBy`:
- Sets the `shiftQuantityForState` field to the `quantity`
value from the documents in each `state`.

- Uses :group:`$shift` to return the `quantity` value
from the document that follows the current document in the output.

- The document position is specified using the :group:`$shift`
`by <shift-by>` `integer` set to `1`.

- For documents outside of the implicit
`window <setWindowFields-window>`, :group:`$shift` returns `"Not available"`, which is specified using the `default <shift-default>` expression.

In this example output, the shifted `quantity` value is shown in the `shiftQuantityForState` field for each returned document:

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "shiftQuantityForState" : 145 }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "shiftQuantityForState" : 120 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "shiftQuantityForState" : "Not available" }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "shiftQuantityForState" : 134 }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "shiftQuantityForState" : 104 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "shiftQuantityForState" : "Not available" }
```

### Shift Using a Negative Integer

This example uses :group:`$shift` in the :pipeline:`$setWindowFields` stage to output the `quantity` of the cake sales from each document before the current document for each `state`:

```javascript
db.cakeSales.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$state",
         sortBy: { quantity: -1 },
         output: {
            shiftQuantityForState: {
               $shift: {
                  output: "$quantity",
                  by: -1,
                  default: "Not available"
               }
            }
         }
      }
   }
] )
```

In the example:

.. include:: /includes/setWindowFields-partition-sort-quantity.rst

- `output` after `sortBy`:
- Sets the `shiftQuantityForState` field to the `quantity`
value from the documents in each `state`.

- Uses :group:`$shift` to return the `quantity` value
from the document before the current document in the output.

- The document position is specified using the :group:`$shift`
`by <shift-by>` `integer` set to `-1`.

- For documents outside of the implicit
`window <setWindowFields-window>`, :group:`$shift` returns `"Not available"`, which is specified using the `default <shift-default>` expression.

In this example output, the shifted `quantity` value is shown in the `shiftQuantityForState` field for each returned document:

```javascript
{ "_id" : 4, "type" : "strawberry", "orderDate" : ISODate("2019-05-18T16:09:01Z"),
  "state" : "CA", "price" : 41, "quantity" : 162, "shiftQuantityForState" : "Not available" }
{ "_id" : 2, "type" : "vanilla", "orderDate" : ISODate("2021-01-11T06:31:15Z"),
  "state" : "CA", "price" : 12, "quantity" : 145, "shiftQuantityForState" : 162 }
{ "_id" : 0, "type" : "chocolate", "orderDate" : ISODate("2020-05-18T14:10:30Z"),
  "state" : "CA", "price" : 13, "quantity" : 120, "shiftQuantityForState" : 145 }
{ "_id" : 1, "type" : "chocolate", "orderDate" : ISODate("2021-03-20T11:30:05Z"),
  "state" : "WA", "price" : 14, "quantity" : 140, "shiftQuantityForState" : "Not available" }
{ "_id" : 5, "type" : "strawberry", "orderDate" : ISODate("2019-01-08T06:12:03Z"),
  "state" : "WA", "price" : 43, "quantity" : 134, "shiftQuantityForState" : 140 }
{ "_id" : 3, "type" : "vanilla", "orderDate" : ISODate("2020-02-08T13:13:23Z"),
  "state" : "WA", "price" : 13, "quantity" : 104, "shiftQuantityForState" : 134 }
```
