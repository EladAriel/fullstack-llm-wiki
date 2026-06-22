---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/in.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $in (expression operator)

## Definition

## Behavior

:expression:`$in` fails with an error in either of the following cases: if the $in expression is not given exactly two arguments, or if the second argument does not resolve to an array.

## Example

A collection named `fruit` has the following documents:

```javascript
{ "_id" : 1, "location" : "24th Street",
  "in_stock" : [ "apples", "oranges", "bananas" ] }
{ "_id" : 2, "location" : "36th Street",
  "in_stock" : [ "bananas", "pears", "grapes" ] }
{ "_id" : 3, "location" : "82nd Street",
  "in_stock" : [ "cantaloupes", "watermelons", "apples" ] }
```

The following aggregation operation looks at the `in_stock` array in each document and determines whether the string `bananas` is present.

```javascript
db.fruit.aggregate([
  {
    $project: {
      "store location" : "$location",
      "has bananas" : {
        $in: [ "bananas", "$in_stock" ]
      }
    }
  }
])
```

The operation returns the following results:

```javascript
{ "_id" : 1, "store location" : "24th Street", "has bananas" : true }
{ "_id" : 2, "store location" : "36th Street", "has bananas" : true }
{ "_id" : 3, "store location" : "82nd Street", "has bananas" : false }
```
