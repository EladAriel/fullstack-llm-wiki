---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/isoWeek.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $isoWeek (expression operator)

## Definition

## Behavior

> **Note:**

## Example

A collection called `deliveries` contains the following documents:

```javascript
db.deliveries.insertMany( [
   { _id: 1, date: ISODate("2006-10-24T00:00:00Z"), city: "Boston" },
   { _id: 2, date: ISODate("2011-08-18T00:00:00Z"), city: "Detroit" }
] )
```

The following operation returns the week number for each `date` field.

```javascript
db.deliveries.aggregate( [
  {
    $project: {
      _id: 0,
      city: "$city",
      weekNumber: { $isoWeek: "$date" }
    }
  }
] )
```

The operation returns the following results:

```javascript
[
   { city: "Boston", weekNumber: 43 },
   { city: "Detroit", weekNumber: 33 }
]
```

> **Seealso:** - `/reference/operator/aggregation/isoDayOfWeek`
- `/reference/operator/aggregation/isoWeekYear`
