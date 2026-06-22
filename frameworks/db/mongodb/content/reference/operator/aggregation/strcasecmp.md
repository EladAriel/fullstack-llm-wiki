---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/strcasecmp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# $strcasecmp (expression operator)

## Definition

## Behavior

.. include:: /includes/intro-aggregation-string.rst

For a case sensitive comparison, see :expression:`$cmp`.

## Example

Consider a `inventory` collection with the following documents:

```javascript
db.inventory.insertMany( [
   { _id: 1, item: "ABC1", quarter: "13Q1", description: "product 1" },
   { _id: 2, item: "ABC2", quarter: "13Q4", description: "product 2" },
   { _id: 3, item: "XYZ1", quarter: "14Q2", description: null } 
] )
```

The following operation uses the :expression:`$strcasecmp` operator to perform case-insensitive comparison of the `quarter` field value to the string `"13q4"`:

```javascript
db.inventory.aggregate(
   [
     {
       $project:
          {
            item: 1,
            comparisonResult: { $strcasecmp: [ "$quarter", "13q4" ] }
          }
      }
   ]
)
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", comparisonResult: -1 }
{ _id: 2, item: "ABC2", comparisonResult: 0 }
{ _id: 3, item: "XYZ1", comparisonResult: 1 }
```
