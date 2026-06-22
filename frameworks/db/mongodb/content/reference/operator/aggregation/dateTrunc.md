---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/dateTrunc.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $dateTrunc (expression operator)

## Definition

.. versionadded:: 5.0

Truncates a date.

:expression:`$dateTrunc` syntax:

```none
{
   $dateTrunc: {
      date: <Expression>,
      unit: <Expression>,
      binSize: <Expression>,
      timezone: <tzExpression>,
      startOfWeek: <Expression>
   }
}
```

> **Seealso:** - `aggregation-expressions`
- `bson-types`

## Behavior

:expression:`$dateTrunc`:

- Returns `null` if:
- any of the input fields except :ref:`startOfWeek
<dateTrunc-startOfWeek>` is missing or set to `null`, or

- if `unit <dateTrunc-unit>` is `week` and :ref:`startOfWeek
<dateTrunc-startOfWeek>` is missing or set to `null`.

- Uses the :wikipedia:`proleptic Gregorian calendar
<Proleptic_Gregorian_calendar>` for dates preceding the year 1583.

- Accounts for Daylight Savings Time, but does not account for
:wikipedia:`leap seconds <Leap_second>`.

### `binSize` and `unit` Fields

.. include:: /includes/dateTrunc-binSize-unit.rst

For example:

- If `binSize <dateTrunc-binSize>` is `1` and :ref:`unit
<dateTrunc-unit>` is `hour`, the time period is one hour. For the `date <dateTrunc-date>` `2021-03-20T11:30:05Z`, :expression:`$dateTrunc` returns `2021-03-20T11:00:00Z`.

- If `binSize <dateTrunc-binSize>` is `2` and :ref:`unit
<dateTrunc-unit>` is `hour`, the time period is two hours. For the `date <dateTrunc-date>` `2021-03-20T11:30:05Z`, :expression:`$dateTrunc` returns `2021-03-20T10:00:00Z`.

:expression:`$dateTrunc`:

- Divides the time for the :expression:`$dateTrunc` calculation into
`binSize <dateTrunc-binSize>` time periods in the specified time `unit <dateTrunc-unit>`.

The time periods start at a reference date, which is determined by `unit <dateTrunc-unit>`. If `unit <dateTrunc-unit>` is:

- A string other than `week`, :expression:`$dateTrunc` uses
a reference date of `2000-01-01T00:00:00.00Z`. For example, if `binSize <dateTrunc-binSize>` is `10` and `unit <dateTrunc-unit>` is `year`, example time periods are:

- `2000-01-01T00:00:00.00Z`
- `2010-01-01T00:00:00.00Z`
- `2020-01-01T00:00:00.00Z`
- Equal to `week`, :expression:`$dateTrunc` uses a reference
date that is set to the earliest first day of the week that is greater than or equal to `2000-01-01`. The first day is set using `startOfWeek <dateTrunc-startOfWeek>` (the default is Sunday).

- Returns the lower boundary of the time period that the :ref:`date
<dateTrunc-date>` is in. The boundary is returned as an `ISODate`. If the `binSize <dateTrunc-binSize>` field is `1`, :expression:`$dateTrunc` sets the least significant parts (as determined by `unit <dateTrunc-unit>`) of the returned `ISODate` to `0` and keeps the rest of the `ISODate` the same.

If `unit <dateTrunc-unit>` is:

- `year`: :expression:`$dateTrunc` returns the `ISODate` for the
start of January 1 for the year in `date <dateTrunc-date>`.

- `quarter`: :expression:`$dateTrunc` returns the `ISODate` for
the start of the first day of the calendar quarter in `date <dateTrunc-date>`.

The quarters are:

- January to March
- April to June
- July to September
- October to December
- `month`: :expression:`$dateTrunc` returns the `ISODate` for
the start of the first day of the month in `date <dateTrunc-date>`.

- `week`: :expression:`$dateTrunc` returns the `ISODate` for the
start of the `startOfWeek <dateTrunc-startOfWeek>` day in `date <dateTrunc-date>`. The default for `startOfWeek <dateTrunc-startOfWeek>` is Sunday.

- `day`: :expression:`$dateTrunc` returns the `ISODate` for the
start of the day in `date <dateTrunc-date>`.

- `hour`: :expression:`$dateTrunc` returns the `ISODate` for the
start of the hour in `date <dateTrunc-date>`.

- `minute`: :expression:`$dateTrunc` returns the `ISODate` for
the start of the minute in `date <dateTrunc-date>`.

- `second`: :expression:`$dateTrunc` returns the `ISODate`
for start of the second in `date <dateTrunc-date>`.

### `unit` and `startOfWeek` Fields

If `unit <dateTrunc-unit>` is:

- A string other than `week`, :ref:`startOfWeek
<dateTrunc-startOfWeek>` is ignored.

- Equal to `week` and `startOfWeek <dateTrunc-startOfWeek>` is:
- Specified: :expression:`$dateTrunc` uses :ref:`startOfWeek
<dateTrunc-startOfWeek>` as the first day of the week for the calculation.

- Omitted: :expression:`$dateTrunc` uses Sunday as the start of the
week for the calculation.

## Examples

.. include:: /includes/cakeSales-example-collection.rst

The `cakeSales` collection is used in the following examples.

### Truncate Order Dates in a `$project` Pipeline Stage

This example uses :expression:`$dateTrunc` in a :pipeline:`$project` stage to truncate the cake sales `orderDate` values to two weeks:

```javascript
db.cakeSales.aggregate( [
   {
      $project: {
         _id: 1,
         orderDate: 1,
         truncatedOrderDate: {
            $dateTrunc: {
               date: "$orderDate", unit: "week", binSize: 2,
               timezone: "America/Los_Angeles", startOfWeek: "Monday"
            }
         }
      }
   }
] )
```

In the example:

- `$project includes the id`, `orderDate`, and
`truncatedOrderDate` fields in the output.

- `$dateTrunc` truncates the `orderDate` field to a `2`
`binSize <dateTrunc-binSize>` `week` `unit <dateTrunc-unit>` time period in the `America/Los_Angeles` `timezone <dateTrunc-timezone>` with `startOfWeek <dateTrunc-startOfWeek>` set to `Monday`.

In this example output, the truncated `orderDate` is shown in the `truncatedOrderDate` field:

```javascript
[
   {
      _id: 0,
      orderDate: ISODate("2020-05-18T14:10:30.000Z"),
      truncatedOrderDate: ISODate("2020-05-11T07:00:00.000Z")
   },
   {
      _id: 1,
      orderDate: ISODate("2021-03-20T11:30:05.000Z"),
      truncatedOrderDate: ISODate("2021-03-15T07:00:00.000Z")
   },
   {
      _id: 2,
      orderDate: ISODate("2021-01-11T06:31:15.000Z"),
      truncatedOrderDate: ISODate("2021-01-04T08:00:00.000Z")
   },
   {
      _id: 3,
      orderDate: ISODate("2020-02-08T13:13:23.000Z"),
      truncatedOrderDate: ISODate("2020-02-03T08:00:00.000Z")
   },
   {
      _id: 4,
      orderDate: ISODate("2019-05-18T16:09:01.000Z"),
      truncatedOrderDate: ISODate("2019-05-13T07:00:00.000Z")
   },
   {
      _id: 5,
      orderDate: ISODate("2019-01-08T06:12:03.000Z"),
      truncatedOrderDate: ISODate("2019-01-07T08:00:00.000Z")
   }
]
```

### Truncate Order Dates and Obtain Quantity Sum in a `$group` Pipeline Stage

This example uses :expression:`$dateTrunc` in a :pipeline:`$group` stage to truncate the cake sales `orderDate` values to six months and return the sum of the `quantity` values:

```javascript
db.cakeSales.aggregate( [
   {
      $group: {
         _id: {
            truncatedOrderDate: {
               $dateTrunc: {
                  date: "$orderDate", unit: "month", binSize: 6
               }
            }
         },
         sumQuantity: { $sum: "$quantity" }
      }
   }
] )
```

In the example:

- `$group has the id` field set to the `truncatedOrderDate`
field to group the `cakeSales` documents, and returns the sum of the `quantity` values for each group using :group:`$sum`.

- `$dateTrunc` truncates the `orderDate` field to a `6`
`binSize <dateTrunc-binSize>` `month` `unit <dateTrunc-unit>` time period.

In this example output, the truncated `orderDate` is shown in the `truncatedOrderDate` field and the `quantity` sum is shown in the `sumQuantity` field:

```javascript
[
   {
      _id: { truncatedOrderDate: ISODate("2020-01-01T00:00:00.000Z") },
      sumQuantity: 224
   },
   {
      _id: { truncatedOrderDate: ISODate("2021-01-01T00:00:00.000Z") },
      sumQuantity: 285
   },
   {
      _id: { truncatedOrderDate: ISODate("2019-01-01T00:00:00.000Z") },
      sumQuantity: 296
   }
]
```
