---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/dateAdd.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $dateAdd (expression operator)

## Definition

## Behavior

### Time Measurement

MongoDB follows prevaling database usage and works with time in UTC. The `dateAdd` expression always takes a `startDate` in UTC and returns a result in UTC. If the `timezone` is specified, the calculation will be done using the specified `timezone`. The timezone is especially important when a calculation involves Daylight Savings Time (DST).

If the `unit` is a `month`, or larger the operation adjusts to account for the last day of the month. Adding one `month` on the last day of October, for example, demonstrates the "last-day-of-the-month" adjustment.

```javascript
{
   $dateAdd:
      {
         startDate: ISODate("2020-10-31T12:10:05Z"),
         unit: "month",
         amount: 1
      }
}
```

Notice that the date returned, `ISODate("2020-11-30T12:10:05Z")`, is the 30th and not the 31st since November has fewer days than October.

### Time Zone

.. include:: /includes/fact-olson-tz-behavior.rst

## Examples

### Add a Future Date

Consider a collection of customer orders with these documents:

```javascript
db.shipping.insertMany(
  [
     { custId: 456, purchaseDate: ISODate("2020-12-31") },
     { custId: 457, purchaseDate: ISODate("2021-02-28") },
     { custId: 458, purchaseDate: ISODate("2021-02-26") }
  ]
)
```

The normal shipping time is 3 days. You can use `$dateAdd` in an aggregation pipeline to set an `expectedDeliveryDate` 3 days in the future.

```javascript
db.shipping.aggregate(
   [
      {
         $project:
            {
               expectedDeliveryDate:
                  {
                     $dateAdd:
                        {
                           startDate: "$purchaseDate",
                           unit: "day",
                           amount: 3
                        }
                  }
            }
       },
       { 
          $merge: "shipping" 
       }
    ]
 )
```

After adding 3 days to the `purchaseDate` with `$dateAdd` in the :pipeline:`$project` stage, the :pipeline:`$merge` stage updates the original documents with the `expectedDeliveryDate`.

The resulting documents look like this:

```javascript
{
   "_id" : ObjectId("603dd4b2044b995ad331c0b2"),
   "custId" : 456,
   "purchaseDate" : ISODate("2020-12-31T00:00:00Z"),
   "expectedDeliveryDate" : ISODate("2021-01-03T00:00:00Z")
}
{
   "_id" : ObjectId("603dd4b2044b995ad331c0b3"),
   "custId" : 457,
   "purchaseDate" : ISODate("2021-02-28T00:00:00Z"),
   "expectedDeliveryDate" : ISODate("2021-03-03T00:00:00Z")
}
{
    "_id" : ObjectId("603dd4b2044b995ad331c0b4"),
   "custId" : 458,
   "purchaseDate" : ISODate("2021-02-26T00:00:00Z"),
   "expectedDeliveryDate" : ISODate("2021-03-01T00:00:00Z")
}
```

### Filter on a Date Range

Update the `shipping` collection from the last example with this code to add delivery dates to the documents:

```javascript
db.shipping.updateOne(
   { custId: 456 },
   { $set: { deliveryDate: ISODate( "2021-01-10" ) } }
)

db.shipping.updateOne(
  { custId: 457 },
  { $set: { deliveryDate:  ISODate( "2021-03-01" ) } }
)

db.shipping.updateOne(
   { custId: 458 },
   { $set: { deliveryDate:  ISODate( "2021-03-02" ) } }
)
```

You want to find late shipments. Use `$dateAdd` in a :pipeline:`$match` stage to create a filter that matches documents in a range of dates defined by a starting point (`$purchaseDate`) and a time period given by `$dateAdd`.

```javascript
db.shipping.aggregate(
   [
      {
         $match: 
            {
               $expr:
                  {
                     $gt:
                        [ "$deliveryDate",
                          { 
                             $dateAdd:
                                { 
                                   startDate: "$purchaseDate",
                                   unit: "day",
                                   amount: 5
                                } 
                           }
                        ]
                  }
            }
       },
       { 
          $project: 
             {
                _id: 0,
                custId: 1,
                purchased:
                   {
                       $dateToString: 
                          {
                             format: "%Y-%m-%d",
                             date: "$purchaseDate"
                          }
                   },
                delivery:
                   {
                      $dateToString:
                         {
                            format: "%Y-%m-%d",
                            date: "$deliveryDate"
                         }
                   }
             }
       } 
   ]
) 
```

The :pipeline:`$match` stage uses :expression:`$gt` and `$dateAdd` in an expression (:query:`$expr`) to compare the actual `deliveryDate` with an expected date. Documents with delivery dates more than 5 days after the `purchaseDate` are passed on to the :pipeline:`$project` stage.

The :pipeline:`$project` stage uses the :expression:`$dateToString` expression to convert the dates to a more readable format. Without the conversion, MongoDB returns the date in `ISODate` format and assumes a UTC timezone.

In this example only one record is returned:

```javascript
{ "custId" : 456, "purchased" : "2020-12-31", "delivery" : "2021-01-10" }
```

### Adjust for Daylight Savings Time

All dates are stored internally in UTC time. When a `timezone` is specified, `$dateAdd` uses local time to carry out the calculations. The results are displayed in UTC.

You have customers in several timezones and you want to see what effect daylight savings time might have on your billing periods if you bill by `day` or by `hour`.

Create this collection of connection times:

```javascript
db.billing.insertMany(
   [
      {
         location: "America/New_York",
         login: ISODate("2021-03-13T10:00:00-0500"),
         logout: ISODate("2021-03-14T18:00:00-0500")
      },
      {
         location: "America/Mexico_City",
         login: ISODate("2021-03-13T10:00:00-00:00"),
         logout: ISODate("2021-03-14T08:00:00-0500")
      }
   ]
)
```

First add 1 day, then add 24 hours to the `login` dates in each document.

```javascript
db.billing.aggregate(
   [
      {
         $project:
            {
               _id: 0,
               location: 1,
               start:
                  {
                     $dateToString:
                        {
                           format: "%Y-%m-%d %H:%M",
                           date: "$login"
                        }
                  },
               days:
                  {
                     $dateToString: 
                        {
                           format: "%Y-%m-%d %H:%M", 
                           date: 
                              {
                                 $dateAdd:
                                    {
                                       startDate: "$login",
                                       unit: "day",
                                       amount: 1,
                                       timezone: "$location"
                                    }
                              }
                        }
                  },
               hours:
                  {
                     $dateToString:
                        {
                           format: "%Y-%m-%d %H:%M",
                           date:
                              {
                                 $dateAdd:
                                 {
                                    startDate: "$login",
                                    unit: "hour",
                                    amount: 24,
                                    timezone: "$location"
                                 }
                              }
                        }
                  },
               startTZInfo:
                  {
                     $dateToString:
                        {
                           format: "%Y-%m-%d %H:%M",
                           date: "$login",
                           timezone: "$location"
                        }
                  },
               daysTZInfo:
                  {
                     $dateToString:
                        {
                           format: "%Y-%m-%d %H:%M",
                           date:
                              {
                                 $dateAdd:
                                    {
                                       startDate: "$login",
                                       unit: "day",
                                       amount: 1,
                                       timezone: "$location"
                                    }
                              },
                           timezone: "$location"
                        }
                  },
               hoursTZInfo:
                  {
                     $dateToString:
                        {
                           format: "%Y-%m-%d %H:%M",
                           date:
                              {
                                 $dateAdd:
                                    {
                                       startDate: "$login",
                                       unit: "hour",
                                       amount: 24,
                                       timezone: "$location"
                                    }
                              },
                           timezone: "$location"
                        }
                  },
            }
      }
   ]
).pretty()
```

The :expression:`$dateToString` expression reformats the output for readability. Results are summarized here:

The chart highlights several points:

- Unformatted dates are returned in UTC. The `$login` for New York is
UTC -5, however the `start`, `days`, and `hours` rows display the time in UTC.

- March 14th is the start of DST in New York, but not in Mexico. The
calculated time is adjusted when a location switches to DST and crosses from one `day` to the next.

- DST modifies the length of the `day`, not the `hour`. There is no
DST change for `hours`. There is an only an adjustment for DST when the measurement `unit` is `day` or larger and the computation crosses a clock change in the specified `timezone`.

> **Seealso:** :expression:`$dateSubtract`, :expression:`$dateDiff`
