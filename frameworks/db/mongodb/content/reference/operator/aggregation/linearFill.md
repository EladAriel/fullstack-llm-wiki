---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/linearFill.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# $linearFill (expression operator)

## Definition

## Syntax

The :group:`$linearFill` expression has this syntax:

```none
{ $linearFill: <expression> }
```

For more information on expressions, see `aggregation-expressions`.

## Behavior

:group:`$linearFill` fills `null` and missing fields using |linear-interpolation| based on surrounding non-`null` field values. The surrounding field values are determined by the sort order specified in :pipeline:`$setWindowFields`.

- :group:`$linearFill` fills `null` and missing values proportionally
spanning the value range between surrounding non-`null` values. To determine the values for missing fields, :group:`$linearFill` uses:

- The difference of surrounding non-`null` values.
- The number of `null` fields to fill between the surrounding
values.

- :group:`$linearFill` can fill multiple consecutive `null` values if
those values are preceded and followed by non-`null` values according to the sort order specified in :pipeline:`$setWindowFields`.

- `null` values that are not preceded and followed by non-`null`
values remain `null`.

### Comparison of :pipeline:`$fill` and :group:`$linearFill`

To fill missing field values using :wikipedia:`linear interpolation <Linear_interpolation>`, you can use:

- The :pipeline:`$fill` stage  with `{ method: "linear" }`.
When you use the :pipeline:`$fill` stage, the field you specify in the output is the same field used as the source data. See `fill-example-linear`.

- The :group:`$linearFill` operator inside of a
:pipeline:`$setWindowFields` stage.

When you use the :group:`$linearFill` operator, you can set values for a different field than the field used as the source data. See `linearFill-example-multiple-methods`.

## Examples

The examples on this page use a `stock` collection that contains tracks a single company's stock price at hourly intervals:

```javascript
db.stock.insertMany( [ 
   {
      time: ISODate("2021-03-08T09:00:00.000Z"),
      price: 500
   },
   {
      time: ISODate("2021-03-08T10:00:00.000Z"),
   },
   { 
      time: ISODate("2021-03-08T11:00:00.000Z"),
      price: 515
   },
   {
      time: ISODate("2021-03-08T12:00:00.000Z")
   },
   {
      time: ISODate("2021-03-08T13:00:00.000Z")
   },
   {
      time: ISODate("2021-03-08T14:00:00.000Z"),
      price: 485
   }
] )
```

The `price` field is missing for some of the documents in the collection.

### Fill Missing Values with Linear Interpolation

To populate the missing `price` values using |linear-interpolation|, use :group:`$linearFill` inside of a :pipeline:`$setWindowFields` stage:

```javascript
db.stock.aggregate( [
   {
      $setWindowFields:
         {
            sortBy: { time: 1 },
            output:
               {
                  price: { $linearFill: "$price" }
               }
         }
   }
] )
```

In the example:

- `sortBy: { time: 1 }` sorts the documents by the `time` field in
ascending order, from earliest to latest.

- `output <setWindowFields-output>` specifies:
- `price` as the field for which to fill in missing values.
- `{ $linearFill: "$price" }` as the value for the missing field.
:group:`$linearFill` fills missing `price` values using |linear-interpolation| based on the surrounding `price` values in the sequence.

Example output:

```javascript
[
   {
      _id: ObjectId("620ad555394d47411658b5ef"),
      time: ISODate("2021-03-08T09:00:00.000Z"),
      price: 500
   },
   {
      _id: ObjectId("620ad555394d47411658b5f0"),
      time: ISODate("2021-03-08T10:00:00.000Z"),
      price: 507.5
   },
   {
      _id: ObjectId("620ad555394d47411658b5f1"),
      time: ISODate("2021-03-08T11:00:00.000Z"),
      price: 515
   },
   {
      _id: ObjectId("620ad555394d47411658b5f2"),
      time: ISODate("2021-03-08T12:00:00.000Z"),
      price: 505
   },
   {
      _id: ObjectId("620ad555394d47411658b5f3"),
      time: ISODate("2021-03-08T13:00:00.000Z"),
      price: 495
   },
   {
      _id: ObjectId("620ad555394d47411658b5f4"),
      time: ISODate("2021-03-08T14:00:00.000Z"),
      price: 485
   }
]
```

### Use Multiple Fill Methods in a Single Stage

.. include:: /includes/example-multiple-fill-methods.rst

## Restrictions

- To use :group:`$linearFill`, you must use the :ref:`sortBy
<setWindowFields-sortBy>` field to sort your data.

- When using :group:`$linearFill` window function,
:pipeline:`$setWindowFields` returns an error if there are any repeated values in the `sortBy <setWindowFields-sortBy>` field in a single `partition <setWindowFields-partitionBy>`.
