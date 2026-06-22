---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/count.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $count (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

:pipeline:`$count` has the following syntax:

```javascript
{ $count: <string> }
```

`<string>` is the name of the output field which has the count as its value. `<string>` must be a non-empty string, must not start with `$` and must not contain the `.` character.

## Behavior

The return type is represented by the smallest type that can store the final value of count: :bsontype:`integer <Int32>` → :bsontype:`long <Int64>` → :bsontype:`double <Double>`

The :pipeline:`$count` stage is equivalent to the following :pipeline:`$group` and :pipeline:`$project` sequence:

```javascript
db.collection.aggregate( [
   { $group: { _id: null, myCount: { $sum: 1 } } },
   { $project: { _id: 0 } }
] )
```

`myCount` is the output field that stores the count. You can specify another name for the output field.

If the input dataset is empty, `$count` doesn't return a result.

> **Seealso:** :method:`db.collection.countDocuments()` wraps the :pipeline:`$group`
aggregation stage with a :group:`$sum` expression.

## Examples

## Learn More

- :method:`db.collection.countDocuments()`
- :pipeline:`$collStats`
- :method:`db.collection.estimatedDocumentCount()`
- :dbcommand:`count`
- :method:`db.collection.count()`
