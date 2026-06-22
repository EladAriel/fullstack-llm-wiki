---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/derivative.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================================

# $derivative (Window Function) (expression operator)

## Definition

.. versionadded:: 5.0

Returns the average rate of change within the specified `window <setWindowFields-window>`, which is calculated using the:

- First and last documents in the :pipeline:`$setWindowFields` stage
`window <setWindowFields-window>`.

- Numerator, which is set to the result of subtracting the numeric
`expression <aggregation-expressions>` value for the first document from the `expression <aggregation-expressions>` value for the last document.

- Denominator, which is set to the result of subtracting the
`sortBy <setWindowFields-sortBy>` field value for the first document from the `sortBy <setWindowFields-sortBy>` field value for the last document.

:group:`$derivative` is only available in the :pipeline:`$setWindowFields` stage. You must specify a `window <setWindowFields-window>` in the :pipeline:`$setWindowFields` stage when using :group:`$derivative`.

:group:`$derivative` syntax:

```none
{
   $derivative: {
      input: <expression>,
      unit: <time unit>
   }
} 
```

:group:`$derivative` takes a document with these fields:

## Behavior

You must specify a `window <setWindowFields-window>` in the :pipeline:`$setWindowFields` stage when using :group:`$derivative`.

## Example

Create a `deliveryFleet` collection that contains odometer readings for delivery trucks recorded at 30 second intervals:

```javascript
db.deliveryFleet.insertMany( [
   { truckID: "1", timeStamp: new Date( "2020-05-18T14:10:30Z" ), miles: 1295.1 },
   { truckID: "1", timeStamp: new Date( "2020-05-18T14:11:00Z" ), miles: 1295.63 },
   { truckID: "1", timeStamp: new Date( "2020-05-18T14:11:30Z" ), miles: 1296.25 },
   { truckID: "1", timeStamp: new Date( "2020-05-18T14:12:00Z" ), miles: 1296.76 },
   { truckID: "2", timeStamp: new Date( "2020-05-18T14:10:30Z" ), miles: 10234.1 },
   { truckID: "2", timeStamp: new Date( "2020-05-18T14:11:00Z" ), miles: 10234.33 },
   { truckID: "2", timeStamp: new Date( "2020-05-18T14:11:30Z" ), miles: 10234.73 },
   { truckID: "2", timeStamp: new Date( "2020-05-18T14:12:00Z" ), miles: 10235.13 }
] )
```

This example uses :group:`$derivative` in the :pipeline:`$setWindowFields` stage to obtain the average speed in miles per hour for each truck, and the :pipeline:`$match` stage to filter the results to trucks whose speed exceeded 50 miles per hour:

```javascript
db.deliveryFleet.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$truckID",
         sortBy: { timeStamp: 1 },
         output: {
            truckAverageSpeed: {
               $derivative: {
                  input: "$miles",
                  unit: "hour"
               },
               window: {
                  range: [ -30, 0 ],
                  unit: "second"
               }
            }
         }
      }
   },
   {
      $match: {
         truckAverageSpeed: {
            $gt: 50
         }
      }
   }
] )
```

In the example:

- The :pipeline:`$setWindowFields` stage obtains the average speed in
miles per hour for each truck:

- `partitionBy: "$truckID"` :ref:`partitions
<setWindowFields-partitionBy>` the documents in the collection by `truckID`.

- `sortBy: { timeStamp: 1 }` :ref:`sorts
<setWindowFields-sortBy>` the documents in each partition by `timeStamp` in ascending order (`1`), so the earliest odometer reading is first.

- `output` sets the `miles` derivative value in a new
field called `truckAverageSpeed` using :group:`$derivative` that is run in a `range <setWindowFields-range>` window.

- The `input <derivative-input>` expression is set to
`"$miles"`, which is used in the numerator for the derivative calculation.

- The :group:`$derivative` `unit <derivative-unit>` is set to
`"hour"` for the `timeStamp` field, which is used in the denominator for the derivative calculation.

- The `window <setWindowFields-window>` contains the
`range <setWindowFields-range>` between a lower limit of `-30` seconds (the previous 30 seconds from the current document in the output) and `0` seconds (matches the current document's `timeStamp` value in the output). This means :group:`$derivative` returns the average speed for each truck in miles per hour in the 30 second window.

- The :pipeline:`$match` stage uses the greater than operator
:expression:`$gt` to filter the results to trucks whose speed exceeded 50 miles per hour.

In the following example output, the speed for truck 1 is shown in the `truckAverageSpeed` field. The speed for truck 2 is not shown because truck 2 did not exceed 50 miles per hour.

```javascript
{ "_id" : ObjectId("60cb8a7e833dfeadc8e6285c"), "truckID" : "1",
  "timeStamp" : ISODate("2020-05-18T14:11:00Z"), "miles" : 1295.63,
  "truckAverageSpeed" : 63.60000000002401 }
{ "_id" : ObjectId("60cb8a7e833dfeadc8e6285d"), "truckID" : "1",
  "timeStamp" : ISODate("2020-05-18T14:11:30Z"), "miles" : 1296.25,
  "truckAverageSpeed" : 74.3999999999869 }
{ "_id" : ObjectId("60cb8a7e833dfeadc8e6285e"), "truckID" : "1",
  "timeStamp" : ISODate("2020-05-18T14:12:00Z"), "miles" : 1296.76,
  "truckAverageSpeed" : 61.199999999998916 }
```
