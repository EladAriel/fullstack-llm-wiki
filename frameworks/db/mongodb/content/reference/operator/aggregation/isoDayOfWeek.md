---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/isoDayOfWeek.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
