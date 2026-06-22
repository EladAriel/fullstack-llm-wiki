---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/maxN-array-element.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $maxN (expression operator)

## Definition

> **Seealso:** :expression:`$minN`

## Syntax

:expression:`$maxN` has the following syntax:

```javascript
{ $maxN: { n: <expression>, input: <expression> } }
```

## Behavior

- You cannot specify a value of `n` less than `1`.
- :expression:`$maxN` filters out `null` values found in the `input`
array.

- If the specified `n` is greater than or equal to the number of elements
in the `input` array, :expression:`$maxN` returns all elements in the `input` array.

- If `input` resolves to a non-array value, the aggregation
operation errors.

- If `input` contains both numeric and string elements, the string elements
are sorted before numeric elements according to the `BSON comparison order <bson-types-comparison-order>`.

## Example

Create a `scores` collection with the following documents:

```javascript
db.scores.insertMany([
    { "playerId" : 1, "score" : [ 1, 2, 3 ] },
    { "playerId" : 2, "score" : [ 12, 90, 7, 89, 8 ] },
    { "playerId" : 3, "score" : [ null ] },
    { "playerId" : 4, "score" : [ ] }
    { "playerId" : 5, "score" : [ 1293, "2", 3489, 9 ]}
])
```

The following example uses the :expression:`$maxN` operator to retrieve the two highest scores for each player. The highest scores are returned in the new field `maxScores` created by :pipeline:`$addFields`.

```javascript
db.scores.aggregate([
   { $addFields: { maxScores: { $maxN: { n: 2, input: "$score" } } } }
])
```

The operation returns the following results:

```javascript
[{
  "playerId": 1,
  "score": [ 1, 2, 3 ],
  "maxScores": [ 3, 2 ]
},
{
  "playerId": 2,
  "score": [ 12, 90, 7, 89, 8 ],
  "maxScores": [ 90, 89 ]
},
{
  "playerId": 3,
  "score": [ null ],
  "maxScores": [ ]
},
{
  "playerId": 4,
  "score": [ ],
  "maxScores": [ ]
},
{ 
  "playerId": 5,
  "score": [ 1293, "2", 3489, 9 ],
  "maxScores": [ "2", 3489 ]
}]
```
