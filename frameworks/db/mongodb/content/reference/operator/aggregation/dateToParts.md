---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/dateToParts.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $dateToParts (expression operator)

## Definition

## Behavior

.. include:: /includes/fact-olson-tz-behavior.rst

## Example

Consider a `sales` collection with the following document:

```javascript
{
  "_id" : 2,
  "item" : "abc",
  "price" : 10,
  "quantity" : 2,
  "date" : ISODate("2017-01-01T01:29:09.123Z")
}
```

The following aggregation uses :expression:`$dateToParts` to return a document that contains the constituent parts of the `date` field.

```javascript
db.sales.aggregate([
{
   $project: {
      date: {
         $dateToParts: { date: "$date" } 
      },
      date_iso: { 
         $dateToParts: { date: "$date", iso8601: true }
      },
      date_timezone: {
         $dateToParts: { date: "$date", timezone: "America/New_York" }
      }  
   }
}])
```

The operation returns the following result:

```javascript
{
   "_id" : 2,
   "date" : {
      "year" : 2017,
      "month" : 1,
      "day" : 1,
      "hour" : 1,
      "minute" : 29,
      "second" : 9,
      "millisecond" : 123
   },
   "date_iso" : {
      "isoWeekYear" : 2016,
      "isoWeek" : 52,
      "isoDayOfWeek" : 7,
      "hour" : 1,
      "minute" : 29,
      "second" : 9,
      "millisecond" : 123
   },
   "date_timezone" : {
      "year" : 2016,
      "month" : 12,
      "day" : 31,
      "hour" : 20,
      "minute" : 29,
      "second" : 9,
      "millisecond" : 123
   }
}
```
