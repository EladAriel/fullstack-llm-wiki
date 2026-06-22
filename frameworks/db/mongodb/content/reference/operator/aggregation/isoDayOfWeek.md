---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/isoDayOfWeek.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# $isoDayOfWeek (expression operator)

## Definition

## Behavior

> **Note:**

## Example

A collection called `birthdays` contains the following documents:

```javascript
db.birthdays.insertMany( [
   { _id: 1, name: "Betty", birthday: ISODate("1993-09-21T00:00:00Z") },
   { _id: 2, name: "Veronica", birthday: ISODate("1981-11-07T00:00:00Z") }
] )
```

The following operation returns the weekday number for each `birthday` field.

```javascript
db.birthdays.aggregate( [
  {
    $project: {
      _id: 0,
      name: "$name",
      dayOfWeek: { $isoDayOfWeek: "$birthday" }
    }
  }
] )
```

The operation returns the following results:

```javascript
[
   { name: "Betty", dayOfWeek: 2 },
   { name: "Veronica", dayOfWeek: 6 }
]
```

> **Seealso:** - `/reference/operator/aggregation/isoWeekYear`
- `/reference/operator/aggregation/isoWeek`
