---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/dateFromParts.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# $dateFromParts (expression operator)

## Definition

.. |outofrange| replace:

```
If the number specified is outside this range, :expression:`$dateFromParts` 
incorporates the difference in the date calculation. 
See :ref:`dateFromParts-values` for examples.
```

.. |outofrange-4.4| replace:

```
If the number specified is outside this range,
:expression:`$dateFromParts` errors. The lower bound for this value is ``1``.
```

## Behavior

### Value Range

The supported value range for `year` and `isoWeekYear` is `1-9999`.

If the value specified for fields other than `year`, `isoWeekYear`, and `timezone` is outside the valid range, :expression:`$dateFromParts` carries or subtracts the difference from other date parts to calculate the date.

### Value is Greater than the Range

Consider the following :expression:`$dateFromParts` expression where the `month` field value is `14`, which is 2 months greater than the maximum value of 12 months(or 1 year):

```javascript
{ $dateFromParts: { 'year' : 2017, 'month' : 14, 'day': 1, 'hour' : 12  } }
```

The expression calculates the date by increasing the `year` by 1 and setting the `month` to 2 to return:

```javascript
ISODate("2018-02-01T12:00:00Z")
```

### Value is Less than the Range

Consider the following :expression:`$dateFromParts` expression where the `month` field value is `0`, which is 1 month less than the minimum value of 1 month:

```javascript
{ $dateFromParts: { 'year' : 2017, 'month' : 0, 'day': 1, 'hour' : 12  } }
```

The expression calculates the date by decreasing the `year` by 1 and setting the `month` to 12 to return:

```javascript
ISODate("2016-12-01T12:00:00Z")
```

### Time Zone

.. include:: /includes/fact-olson-tz-behavior.rst

## Example

The following aggregation uses :expression:`$dateFromParts` to construct three date objects from the provided input fields:

```javascript
db.sales.aggregate([
{
   $project: {
      date: {
         $dateFromParts: {
            'year' : 2017, 'month' : 2, 'day': 8, 'hour' : 12
         }
      },
      date_iso: {
         $dateFromParts: {
            'isoWeekYear' : 2017, 'isoWeek' : 6, 'isoDayOfWeek' : 3, 'hour' : 12
         }
      },
      date_timezone: {
         $dateFromParts: {
            'year' : 2016, 'month' : 12, 'day' : 31, 'hour' : 23,
            'minute' : 46, 'second' : 12, 'timezone' : 'America/New_York'
         }
      }
   }
}])
```

The operation returns the following result:

```javascript
{
  "_id" : 1,
  "date" : ISODate("2017-02-08T12:00:00Z"),
  "date_iso" : ISODate("2017-02-08T12:00:00Z"),
  "date_timezone" : ISODate("2017-01-01T04:46:12Z")
}
```
