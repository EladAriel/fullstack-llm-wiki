---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/dateDiff.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $dateDiff (expression operator)

## Definition

> **Seealso:** `aggregation-expressions`, `bson-types`.

## Behavior

### No Fractional Units

The `$dateDiff` expression returns the integer difference between the `startDate` and `endDate` measured in the specified `units`. Durations are measured by counting the number of times a unit boundary is passed. For example, two dates that are 18 months apart would return 1 `year` difference instead of 1.5 `years`.

### Start Of Week

The start of the `week` is `Sunday` unless modified by the `startOfWeek` parameter. Any week that begins between the `startDate` and `endDate` on the specified day will be counted. The week count is not bounded by calendar `month` or calendar `year`.

### Time Zone

.. include:: /includes/fact-olson-tz-behavior.rst

### Additional Details

The algorithm calculates the date difference using the Gregorian calendar.

Leap years and daylight savings time are accounted for but not leap seconds.

The difference returned can be negative.

## Examples

### Elapsed Time

Create a collection of customer orders:

```javascript
db.orders.insertMany(
   [
      { 
         custId: 456, 
         purchased: ISODate("2020-12-31"), 
         delivered: ISODate("2021-01-05")
      },
      { 
         custId: 457, 
         purchased: ISODate("2021-02-28"), 
         delivered: ISODate("2021-03-07")
      },
      { 
         custId: 458, 
         purchased: ISODate("2021-02-16"), 
         delivered: ISODate("2021-02-18")
      }
   ]
)
```

The following example:

- Returns the average number of days for a delivery.
- Uses `dateDiff` to calculate the difference between the
`purchased` date and the `delivered` date.

```javascript
 db.orders.aggregate(
    [
       { 
          $group: 
             { 
                 _id: null, 
                 averageTime: 
                    { 
                       $avg:
                          { 
                             $dateDiff: 
                                { 
                                    startDate: "$purchased",
                                    endDate: "$delivered",
                                    unit: "day"
                                } 
                           }
                    }
             }
       },
       {
          $project:
             { 
                _id: 0,
                numDays: 
                   { 
                      $trunc: 
                         [ "$averageTime", 1 ]
                   }
             }
        }
    ]
)
```

The :group:`$avg` accumulator in the :pipeline:`$group` stage uses `$dateDiff` on each document to get the time between the `purchased` and `delivered` dates. The resulting value is returned as `averageTime`.

The decimal portion of the `averageTime` is truncated (:expression:`$trunc`) in the :pipeline:`$project` stage to produce output like this:

```javascript
{ "numDays" : 4.6 }
```

### Result Precision

Create this collection with starting and ending dates for a subscription.

```javascript
db.subscriptions.insertMany(
   [
      { 
         custId: 456,
         start: ISODate("2010-01-01"),
         end: ISODate("2011-01-01")
      },
      {
         custId: 457,
         start: ISODate("2010-01-01"),
         end: ISODate("2011-06-31")
      },
      {
         custId: 458, 
         start: ISODate("2010-03-01"),
         end: ISODate("2010-04-30")
      }
   ]
)
```

The `$dateDiff` expression returns a time difference expressed in integer `units`. There are no fractional parts of a unit. For example, when counting in `years` there are no half years.

In this example, note how changing the `unit` changes the returned precision:

```javascript
db.subscriptions.aggregate(
   [
      {
         $project:
            { 
               Start: "$start",
               End: "$end", 
               years:
                  {
                     $dateDiff:
                        {
                           startDate: "$start",
                           endDate: "$end",
                           unit: "year"
                        }
                  }, 
               months:
                  {
                     $dateDiff:
                        {
                           startDate: "$start",
                           endDate: "$end",
                           unit: "month"
                        }
                  },
               days:
                  {
                     $dateDiff:
                        {
                           startDate: "$start",
                           endDate: "$end",
                           unit: "day"
                        }
                  },
               _id: 0 
            }
       }
   ]
 )
```

The results are summarized in this table:

The count only increments when a new `unit` starts, so 18 months are reported as 1 year in the second row and 60 days are reported as one month in the third row.

### Weeks Per Month

Create a collection of months:

```javascript
db.months.insertMany(
     [
        { 
           month: "January",
           start: ISODate("2021-01-01"),
           end: ISODate("2021-01-31")
        },
        { 
           month: "February",
           start: ISODate("2021-02-01"),
           end: ISODate("2021-02-28")
        },
        {
           month: "March",
           start: ISODate("2021-03-01"),
           end: ISODate("2021-03-31")
        },
     ]
   )
```

You can change the start of each week, and count the resulting number of weeks in each month with the following code:

```javascript
db.months.aggregate(
   [
      {
         $project:
            { 
               wks_default:
                  {
                     $dateDiff:
                        { 
                           startDate: "$start",  
                           endDate: "$end", 
                           unit: "week"
                        }
                  }, 
               wks_monday:
                  {
                     $dateDiff:
                        { 
                           startDate: "$start",
                           endDate: "$end", 
                           unit: "week", 
                           startOfWeek: "Monday"
                        }
                  },
               wks_friday:
                  {
                     $dateDiff:
                        { 
                           startDate: "$start",
                           endDate: "$end",
                           unit: "week",
                           startOfWeek: "fri" 
                        }
                  },
               _id: 0 
            }
       }
   ]
 )
```

The results are summarized in this table:

From the results:

- When the `startOfWeek` is Sunday, the 5th `week` in January, 2021
begins on the 31st.

- Because the 31st is a Sunday and it is between `startDate` and
`endDate`, one `week` is added to the count.

- The `week` count is incremented even when a calendar week finishes
after `endDate` or in the next calendar period.
