---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/isArray.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# $isArray (expression operator)

## Definition

## Behavior

The `<expression>` can be any valid `expression <aggregation-expressions>`. For more information on expressions, see `aggregation-expressions`.

> **Note:** .. include:: /includes/aggregation/fact-arrays-in-arguments.rst

## Example

Create a collection named `warehouses` with the following documents:

```javascript
db.warehouses.insertMany( [
   { _id : 1, instock: [ "chocolate" ], ordered: [ "butter", "apples" ] },
   { _id : 2, instock: [ "apples", "pudding", "pie" ] },
   { _id : 3, instock: [ "pears", "pecans" ], ordered: [ "cherries" ] },
   { _id : 4, instock: [ "ice cream" ], ordered: [ ] }
] )
```

Check if the `instock` and the `ordered` fields are arrays. If both fields are arrays, concatenate them:

```javascript
db.warehouses.aggregate( [
   { $project:
      { items: 
          { $cond:
            {
              if: { $and: [ { $isArray: "$instock" },
                            { $isArray: "$ordered" } 
                          ] },
              then: { $concatArrays: [ "$instock", "$ordered" ] },
              else: "One or more fields is not an array."
            }
          }
      }
   }
] )
```

```javascript
{ _id : 1, items : [ "chocolate", "butter", "apples" ] }
{ _id : 2, items : "One or more fields is not an array." }
{ _id : 3, items : [ "pears", "pecans", "cherries" ] }
{ _id : 4, items : [ "ice cream" ] }
```

> **Seealso:** - :expression:`$cond`
- :expression:`$concatArrays`
