---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/setEquals.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# $setEquals  (expression operator)

## Definition

## Behavior

.. include:: /includes/important-set-operator-semantics.rst

.. include:: /includes/extracts/fact-agg-top-level-expressions-setEquals.rst

## Example

Consider a `bakeryOrders` collection with the following documents:

```javascript
 db.bakeryOrders.insertMany( [
    { _id: 0, cakes: ["chocolate", "vanilla"], cupcakes: ["chocolate", "vanilla"] },
    { _id: 1, cakes: ["chocolate", "vanilla"], cupcakes: ["vanilla", "chocolate"] },
    { _id: 2, cakes: ["chocolate", "chocolate"], cupcakes: ["chocolate"] },
    { _id: 3, cakes: ["vanilla"], cupcakes: ["chocolate"] },
    { _id: 4, cakes: ["vanilla"], cupcakes: [] }
 ] )
```

The following operation uses the :expression:`$setEquals` operator to determine if the `cakes` array and the `cupcakes` array in each order contain the same flavors:

```javascript
db.bakeryOrders.aggregate(
   [
      { 
         $project: { 
            _id: 0, 
            cakes: 1, 
            cupcakes: 1, 
            sameFlavors: { $setEquals: [ "$cakes", "$cupcakes" ] } 
         } 
      }
   ] )
```

> **Note:** The :pipeline:`$project` stage specifies which fields are included
in the output documents. In this example, the :pipeline:`$project`
stage:
- Excludes the `_id` field from the output.
- Includes the `cakes` and `cupcakes` fields in the output.
- Outputs the result of the `$setEquals` operator in a new field
  called `sameFlavors`.

The operation returns the following results:

```javascript
{
 cakes: [ "chocolate", "vanilla" ],
 cupcakes: [ "chocolate", "vanilla" ],
 sameFlavors: true
},
{
 cakes: [ "chocolate", "vanilla" ],
 cupcakes: [ "vanilla", "chocolate" ],
 sameFlavors: true
},
{ 
 cakes: [ "chocolate", "chocolate" ],
 cupcakes: [ "chocolate" ],
 sameFlavors: true
},
{
 cakes: [ "vanilla" ],
 cupcakes: [ "chocolate" ],
 sameFlavors: false
},
{ 
   cakes: [ "vanilla" ], 
   cupcakes: [], 
   sameFlavors: false 
}
```
