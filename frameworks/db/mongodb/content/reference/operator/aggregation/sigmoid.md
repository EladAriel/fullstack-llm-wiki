---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/sigmoid.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================

# $sigmoid  (expression operator)

## Definition

## Example

This example uses a `myScores` collection that contains the following documents:

```javascript
db.myScores.insertMany( [
   { score: 1 },
   { score: 5 },
   {},
   { score: 13 },
   { score: null },
   { score: 21 },
] )
```

The following aggregation pipeline adds a `scaled` field to each document and uses `$sigmoid` to calculate the `scaled` field value:

```javascript
db.myScores.aggregate( [
   { $set: {
      scaled: { $sigmoid: "$score" }
   } }
] )
```

The operation returns the following documents:

```javascript
{ score: 1, scaled: 0.7310585786 }
{ score: 5, scaled: 0.9933071491 }
{ scaled: null }
{ score: 13, scaled: 0.9999977397 }
{ score: null, scaled: null }
{ score: 19, scaled: 0.9999999992 }
```
