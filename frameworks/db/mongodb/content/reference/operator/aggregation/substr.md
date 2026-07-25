---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/substr.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# $substr (expression operator)

## Definition

## Behavior

If `<start>` is a negative number, :expression:`$substr` returns an empty string `""`.

If `<length>` is a negative number, :expression:`$substr` returns a substring that starts at the specified index and includes the rest of the string.

.. include:: /includes/intro-aggregation-string.rst

## Example

Consider an `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", quarter: "13Q1", description: "product 1" },
   { _id: 2, item: "ABC2", quarter: "13Q4", description: "product 2" },
   { _id: 3, item: "XYZ1", quarter: "14Q2", description: null }
] )
```

The following operation uses the :expression:`$substr` operator to separate the `quarter` value into a `yearSubstring` and a `quarterSubstring`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            yearSubstring: { $substr: [ "$quarter", 0, 2 ] },
            quarterSubstring: { $substr: [ "$quarter", 2, -1 ] }
          }
      }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", yearSubstring: "13", quarterSubstring: "Q1" }
{ _id: 2, item: "ABC2", yearSubstring: "13", quarterSubstring: "Q4" }
{ _id: 3, item: "XYZ1", yearSubstring: "14", quarterSubstring: "Q2" }
```
