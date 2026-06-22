---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation-pipeline-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
