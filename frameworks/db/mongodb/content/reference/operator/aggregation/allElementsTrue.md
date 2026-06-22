---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/allElementsTrue.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# $allElementsTrue (expression operator)

## Definition

## Behavior

.. include:: /includes/extracts/fact-agg-top-level-expressions-allElementsTrue.rst

.. include:: /includes/extracts/fact-agg-boolean-allElementsTrue.rst

## Example

Create an example collection named `survey` with the following documents:

```javascript
db.survey.insertMany([
   { "_id" : 1, "responses" : [ true ] },
   { "_id" : 2, "responses" : [ true, false ] },
   { "_id" : 3, "responses" : [ ] },
   { "_id" : 4, "responses" : [ 1, true, "seven" ] },
   { "_id" : 5, "responses" : [ 0 ] },
   { "_id" : 6, "responses" : [ [ ] ] },
   { "_id" : 7, "responses" : [ [ 0 ] ] },
   { "_id" : 8, "responses" : [ [ false ] ] },
   { "_id" : 9, "responses" : [ null ] },
   { "_id" : 10, "responses" : [ undefined ] }
])
```

The following operation uses the :expression:`$allElementsTrue` operator to determine if the `responses` array only contains values that evaluate to `true`:

```javascript
db.survey.aggregate(
   [
     { $project: { responses: 1, isAllTrue: { $allElementsTrue: [ "$responses" ] }, _id: 0 } }
   ]
)
```

The operation returns the following results:

```javascript
{ "responses" : [ true ], "isAllTrue" : true }
{ "responses" : [ true, false ], "isAllTrue" : false }
{ "responses" : [ ], "isAllTrue" : true }
{ "responses" : [ 1, true, "seven" ], "isAllTrue" : true }
{ "responses" : [ 0 ], "isAllTrue" : false }
{ "responses" : [ [ ] ], "isAllTrue" : true }
{ "responses" : [ [ 0 ] ], "isAllTrue" : true }
{ "responses" : [ [ false ] ], "isAllTrue" : true }
{ "responses" : [ null ], "isAllTrue" : false }
{ "responses" : [ undefined ], "isAllTrue" : false }
```
