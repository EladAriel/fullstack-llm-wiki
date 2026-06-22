---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/isoWeekYear.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# $isoWeekYear (expression operator)

## Definition

## Behavior

> **Note:**

## Example

A collection called `anniversaries` contains the following documents:

```javascript
{ "_id" : 1, "date" : ISODate("2016-01-01T00:00:00Z") }
{ "_id" : 2, "date" : ISODate("2016-01-04T00:00:00Z") }
{ "_id" : 3, "date" : ISODate("2015-01-01T00:00:00Z") }
{ "_id" : 4, "date" : ISODate("2014-04-21T00:00:00Z") }
```

The following operation returns the year number in ISO 8601 format for each `date` field.

```javascript
db.anniversaries.aggregate( [
  {
    $project: {
      yearNumber: { $isoWeekYear: "$date" }
    }
  }
] )
```

The operation returns the following results:

```javascript
{ "_id" : 1, "yearNumber" : 2015 }
{ "_id" : 2, "yearNumber" : 2016 }
{ "_id" : 3, "yearNumber" : 2015 }
{ "_id" : 4, "yearNumber" : 2014 }
```

> **Seealso:** - `/reference/operator/aggregation/isoDayOfWeek`
- `/reference/operator/aggregation/isoWeek`
