---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/let.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $let (expression operator)

## Definition

## Behavior

:expression:`$let` can access variables defined outside its expression block, including `system variables <agg-system-variables>`.

If you modify the values of externally defined variables in the `vars` block, the new values take effect only in the `in` expression. Outside of the `in` expression, the variables retain their previous values.

In the `vars` assignment block, the order of the assignment does **not** matter, and the variable assignments only have meaning inside the `in` expression. As such, accessing a variable's value in the `vars` assignment block refers to the value of the variable defined outside the `vars` block and **not** inside the same `vars` block.

For example, consider the following :expression:`$let` expression:

```none
{
  $let:
    {
      vars: { low: 1, high: "$$low" },
      in: { $gt: [ "$$low", "$$high" ] }
    }
}
```

In the `vars` assignment block, `"$$low"` refers to the value of an externally defined variable `low` and not the variable defined in the same `vars` block. If `low` is not defined outside this :expression:`$let` expression block, the expression is invalid.

## Example

A `sales` collection has the following documents:

```javascript
db.sales.insertMany( [
   { _id: 1, price: 10, tax: 0.50, applyDiscount: true },
   { _id: 2, price: 10, tax: 0.25, applyDiscount: false }
] )
```

The following aggregation uses :expression:`$let` in the :pipeline:`$project` pipeline stage to calculate and return the `finalTotal` for each document:

```none
db.sales.aggregate( [
   {
      $project: {
         finalTotal: {
            $let: {
               vars: {
                  total: { $add: [ '$price', '$tax' ] },
                  discounted: { $cond: { if: '$applyDiscount', then: 0.9, else: 1 } }
               },
               in: { $multiply: [ "$$total", "$$discounted" ] }
            }
         }
      }
   }
] )
```

The aggregation returns the following results:

```javascript
{ "_id" : 1, "finalTotal" : 9.450000000000001 }
{ "_id" : 2, "finalTotal" : 10.25 }
```

> **Seealso:** :expression:`$map`
