---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/sql-aggregation-comparison.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# SQL to Aggregation Mapping Chart

files in the includes directory. To change the content of the tables, edit those files.

The `aggregation pipeline <aggregation-pipeline>` maps to many common SQL aggregation operations.

The following table compares common SQL aggregation terms, functions, and concepts with their corresponding MongoDB `aggregation operators <aggregation-pipeline-operator-reference>`:

For a list of all aggregation pipeline and expression operators, see:

- `aggregation-pipeline-operator-reference`
- `aggregation-pipeline-operators`
> **Seealso:** `/reference/sql-comparison`

## Examples

The following table presents a quick reference of SQL aggregation statements and the corresponding MongoDB statements. The examples in the table assume the following conditions:

- The SQL examples assume two tables, `orders` and
`order_lineitem` that join by the `order_lineitem.order_id` and the `orders.id` columns.

- The MongoDB examples assume one collection `orders` that contain
documents of the following prototype:

```javascript
  {
    cust_id: "abc123",
    ord_date: ISODate("2012-11-02T17:04:11.102Z"),
    status: 'A',
    price: 50,
    items: [ { sku: "xxx", qty: 25, price: 1 },
             { sku: "yyy", qty: 25, price: 1 } ]
  }
```

> **Seealso:** - `/reference/sql-comparison`
- :method:`db.collection.aggregate()`
- `aggregation-pipeline-operator-reference`
