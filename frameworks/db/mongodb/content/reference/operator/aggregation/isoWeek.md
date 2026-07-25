---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/isoWeek.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
