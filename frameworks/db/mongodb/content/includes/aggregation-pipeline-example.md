---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation-pipeline-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The following aggregation pipeline example contains two `stages <aggregation-pipeline-operator-reference>` and returns the total order quantity of medium size pizzas grouped by pizza name:

```javascript
db.orders.aggregate( [

   // Stage 1: Filter pizza order documents by pizza size
   {
      $match: { size: "medium" }
   },

   // Stage 2: Group remaining documents by pizza name and calculate total quantity
   {
      $group: { _id: "$name", totalQuantity: { $sum: "$quantity" } }
   }

] )
```

The :pipeline:`$match` stage:

- Filters the pizza order documents to pizzas with a `size` of
`medium`.

- Passes the remaining documents to the :pipeline:`$group` stage.
The :pipeline:`$group` stage:

- Groups the remaining documents by pizza `name`.
- Uses :group:`$sum` to calculate the total order `quantity` for each
pizza `name`. The total is stored in the `totalQuantity` field returned by the aggregation pipeline.
