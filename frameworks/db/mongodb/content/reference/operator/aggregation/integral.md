---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/integral.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $integral (expression operator)

## Definition

.. versionadded:: 5.0

Returns the approximation of the area under a curve, which is calculated using the trapezoidal rule where each set of adjacent documents form a trapezoid using the:

- `sortBy <setWindowFields-sortBy>` field values in the
:pipeline:`$setWindowFields` stage for the integration intervals.

- `input <integral-input>` field :ref:`expression
<aggregation-expressions>` result values in :group:`$integral` for the y axis values.

:group:`$integral` is only available in the :pipeline:`$setWindowFields` stage.

:group:`$integral` syntax:

```none
{
   $integral: {
      input: <expression>,
      unit: <time unit>
   }
} 
```

:group:`$integral` takes a document with these fields:

## Behavior

If you omit a `window <setWindowFields-window>`, a default window with unbounded upper and lower limits is used.

## Example

Create a `powerConsumption` collection that contains electrical power usage in kilowatts measured by meter devices at 30 second intervals:

```javascript
db.powerConsumption.insertMany( [
   { powerMeterID: "1", timeStamp: new Date( "2020-05-18T14:10:30Z" ),
     kilowatts: 2.95 },
   { powerMeterID: "1", timeStamp: new Date( "2020-05-18T14:11:00Z" ),
     kilowatts: 2.7 },
   { powerMeterID: "1", timeStamp: new Date( "2020-05-18T14:11:30Z" ),
     kilowatts: 2.6 },
   { powerMeterID: "1", timeStamp: new Date( "2020-05-18T14:12:00Z" ),
     kilowatts: 2.98 },
   { powerMeterID: "2", timeStamp: new Date( "2020-05-18T14:10:30Z" ),
     kilowatts: 2.5 },
   { powerMeterID: "2", timeStamp: new Date( "2020-05-18T14:11:00Z" ),
     kilowatts: 2.25 },
   { powerMeterID: "2", timeStamp: new Date( "2020-05-18T14:11:30Z" ),
     kilowatts: 2.75 },
   { powerMeterID: "2", timeStamp: new Date( "2020-05-18T14:12:00Z" ),
     kilowatts: 2.82 }
] )
```

This example uses :group:`$integral` in the :pipeline:`$setWindowFields` stage to output the energy consumption in kilowatt-hours measured by each meter device:

```javascript
db.powerConsumption.aggregate( [
   {
      $setWindowFields: {
         partitionBy: "$powerMeterID",
         sortBy: { timeStamp: 1 },
         output: {
            powerMeterKilowattHours: {
               $integral: {
                  input: "$kilowatts",
                  unit: "hour"
               },
               window: {
                  range: [ "unbounded", "current" ],
                  unit: "hour"
               }
            }
         }
      }
   }
] )
```

In the example:

- `partitionBy: "$powerMeterID"` :ref:`partitions
<setWindowFields-partitionBy>` the documents in the collection by `powerMeterID`.

- `sortBy: { timeStamp: 1 }` :ref:`sorts
<setWindowFields-sortBy>` the documents in each partition by `timeStamp` in ascending order (`1`), so the earliest `timeStamp` is first.

- `output` sets the `kilowatts` integral value in a new
field called `powerMeterKilowattHours` using :group:`$integral` that is run in a `range <setWindowFields-range>` window.

- The `input <integral-input>` expression is set to
`"$kilowatts"`, which is used for the y axis values in the integral calculation.

- The :group:`$integral` `unit <integral-unit>` is set to
`"hour"` for the `timeStamp` field, which means :group:`$integral` returns the kilowatt-hours energy consumption.

- The `window <setWindowFields-window>` contains documents
between an `unbounded` lower limit and the `current` document in the output. This means :group:`$integral` returns the total kilowatt-hours energy consumption for the documents from the beginning of the `partition <setWindowFields-partitionBy>`, which is the first data point in the partition for each power meter, to the timestamp of the current document in the output.

In this example output, the energy consumption measured by meters 1 and 2 are shown in the `powerMeterKilowattHours` field:

```javascript
{ "_id" : ObjectId("60cbdc3f833dfeadc8e62863"), "powerMeterID" : "1",
  "timeStamp" : ISODate("2020-05-18T14:10:30Z"), "kilowatts" : 2.95,
  "powerMeterKilowattHours" : 0 }
{ "_id" : ObjectId("60cbdc3f833dfeadc8e62864"), "powerMeterID" : "1",
  "timeStamp" : ISODate("2020-05-18T14:11:00Z"), "kilowatts" : 2.7,
  "powerMeterKilowattHours" : 0.023541666666666666 }
{ "_id" : ObjectId("60cbdc3f833dfeadc8e62865"), "powerMeterID" : "1",
  "timeStamp" : ISODate("2020-05-18T14:11:30Z"), "kilowatts" : 2.6,
  "powerMeterKilowattHours" : 0.045625 }
{ "_id" : ObjectId("60cbdc3f833dfeadc8e62866"), "powerMeterID" : "1",
  "timeStamp" : ISODate("2020-05-18T14:12:00Z"), "kilowatts" : 2.98,
  "powerMeterKilowattHours" : 0.068875 }
{ "_id" : ObjectId("60cbdc3f833dfeadc8e62867"), "powerMeterID" : "2",
  "timeStamp" : ISODate("2020-05-18T14:10:30Z"), "kilowatts" : 2.5,
  "powerMeterKilowattHours" : 0 }
{ "_id" : ObjectId("60cbdc3f833dfeadc8e62868"), "powerMeterID" : "2",
  "timeStamp" : ISODate("2020-05-18T14:11:00Z"), "kilowatts" : 2.25,
  "powerMeterKilowattHours" : 0.019791666666666666 }
{ "_id" : ObjectId("60cbdc3f833dfeadc8e62869"), "powerMeterID" : "2",
  "timeStamp" : ISODate("2020-05-18T14:11:30Z"), "kilowatts" : 2.75,
  "powerMeterKilowattHours" : 0.040625 }
{ "_id" : ObjectId("60cbdc3f833dfeadc8e6286a"), "powerMeterID" : "2",
  "timeStamp" : ISODate("2020-05-18T14:12:00Z"), "kilowatts" : 2.82,
  "powerMeterKilowattHours" : 0.06383333333333334 }
```

> **Seealso:** .. include:: /includes/fact-timeseries-example-aggregation-book.rst
