---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/filter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# $filter (expression operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

:expression:`$filter` has the following syntax:

```javascript
{ 
    $filter: 
      { 
         input: <array>, 
         as: <string>,  
         arrayIndexAs: <string>,
         cond: <expression>,
         limit: <number expression> 
      } 
}
```

For more information on expressions, see `aggregation-expressions`.

## Behavior

## Examples

The following examples use a `sales` collection with these documents:

```javascript
db.sales.insertMany( [
   {
      _id: 0,
      items: [
         { item_id: 43, quantity: 2, price: 10, name: "pen" },
         { item_id: 2, quantity: 1, price: 240, name: "briefcase" }
      ]
   },
   {
      _id: 1,
      items: [
         { item_id: 23, quantity: 3, price: 110, name: "notebook" },
         { item_id: 103, quantity: 4, price: 5, name: "pen" },
         { item_id: 38, quantity: 1, price: 300, name: "printer" }
      ]
   },
   {
      _id: 2,
      items: [
         { item_id: 4, quantity: 1, price: 23, name: "paper" }
      ]
   }
] )
```

### Filter Based on Number Comparison

The following example filters the `items` array to only include documents that have a `price` greater than or equal to `100`:

### Use the limit Field

The example uses the `limit` field to specify the number of matching elements returned in each `items` array.

### limit Greater than Possible Matches

The example uses a `limit` field value that is larger than the possible number of matching elements that can be returned. In this case, `limit` does not affect the query results and returns all documents matching the `$gte` filter criteria.

### Filter Based on String Equality Match

The following aggregation filters for `items` that have a `name` value of `pen`.

### Filter Based on Regular Expression Match

The following aggregation uses :expression:`$regexMatch` to filter for `items` that have a `name` value that starts with `p`:

### Access the Index of Each Item in an Array

.. include:: /includes/people-collection.rst

The following example uses `arrayIndexAs`. The `myIndex` variable has the index of each hobby in the `hobbies` array. The example returns documents with these fields:

- Person name.
- `secondaryHobbies` array that includes every other hobby.
```javascript
db.people.aggregate( [
   {
      $project: {
         _id: 0,
         name: 1,
         secondaryHobbies: {
            $filter: {
               input: "$hobbies",
               arrayIndexAs: "myIndex",
               cond: { $eq: [ { $mod: [ "$$myIndex", 2 ] }, 0 ] }
            }
         }
      }
   }
] )
```

Output:

.. include:: /includes/filter-index-example-output.rst

### Use `$$IDX` to Access the Index

.. include:: /includes/IDX-use.rst

The following example returns the same documents as the example in the previous section `filter-index-example`, but uses `$$IDX` instead of `arrayIndexAs`:

```javascript
db.people.aggregate( [
   {
      $project: {
         _id: 0,
         name: 1,
         secondaryHobbies: {
            $filter: {
               input: "$hobbies",
               cond: { $eq: [ { $mod: [ "$$IDX", 2 ] }, 0 ] }
            }
         }
      }
   }
] )
```
