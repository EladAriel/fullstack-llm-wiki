---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/slice.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# $slice  (expression operator)

## Definition

## Behavior

## Example

A collection named `users` contains the following documents:

```javascript
db.users.insertMany( [
   { _id: 1, name: "dave123", favorites: [ "chocolate", "cake", "butter", "apples" ] },
   { _id: 2, name: "li", favorites: [ "apples", "pudding", "pie" ] },
   { _id: 3, name: "ahn", favorites: [ "pears", "pecans", "chocolate", "cherries" ] },
   { _id: 4, name: "ty", favorites: [ "ice cream" ] }
] )
```

The following example returns at most the first three elements in the `favorites` array for each user:

```javascript
db.users.aggregate([
   { $project: { name: 1, threeFavorites: { $slice: [ "$favorites", 3 ] } } }
])
```

The operation returns the following results:

```javascript
[
   { _id: 1, name: "dave123", threeFavorites: [ "chocolate", "cake", "butter" ] },
   { _id: 2, name: "li", threeFavorites: [ "apples", "pudding", "pie" ] },
   { _id: 3, name: "ahn", threeFavorites: [ "pears", "pecans", "chocolate" ] },
   { _id: 4, name: "ty", threeFavorites: [ "ice cream" ] }
]
```
