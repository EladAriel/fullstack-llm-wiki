---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/dateToString.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================

# $dateToString (expression operator)

## Definition

.. include:: /includes/fact-compatibility.rst

The :expression:`$dateToString` expression has the following `operator expression syntax <aggregation-expressions>`:

```javascript
{ $dateToString: {
    date: <dateExpression>,
    format: <formatString>,
    timezone: <tzExpression>,
    onNull: <expression>
} }
```

> **Seealso:** - :expression:`$toString`
- :expression:`$convert`

## Format Specifiers

.. include:: /includes/extracts/date-format-specifiers-dateToString.rst

## Example

Consider a `sales` collection with the following document:

```javascript
db.sales.insertOne(
 {
  "_id" : 1,
  "item" : "abc",
  "price" : 10,
  "quantity" : 2,
  "date" : ISODate("2014-01-01T08:15:39.736Z")
 } 
)
```

The following aggregation uses `$dateToString` to return the `date` field as formatted strings:

```javascript
db.sales.aggregate(
   [
     {
       $project: {
          yearMonthDayUTC: { $dateToString: { format: "%Y-%m-%d", date: "$date" } },
          timewithOffsetNY: { $dateToString: { format: "%H:%M:%S:%L%z", date: "$date", timezone: "America/New_York"} },
          timewithOffset430: { $dateToString: { format: "%H:%M:%S:%L%z", date: "$date", timezone: "+04:30" } },
          minutesOffsetNY: { $dateToString: { format: "%Z", date: "$date", timezone: "America/New_York" } },
          minutesOffset430: { $dateToString: { format: "%Z", date: "$date", timezone: "+04:30" } },
          abbreviated_month: { $dateToString: {format: "%b", date: "$date", timezone: "+04:30" } },
          full_month: { $dateToString: { format: "%B", date: "$date", timezone: "+04:30" } }
       }
     }
   ]
)
```

The operation returns the following result:

```javascript
{
   "_id" : 1,
   "yearMonthDayUTC" : "2014-01-01",
   "timewithOffsetNY" : "03:15:39:736-0500",
   "timewithOffset430" : "12:45:39:736+0430",
   "minutesOffsetNY" : "-300",
   "minutesOffset430" : "270",
   "abbreviated_month": "Jan",
   "full_month": "January"
}
```
