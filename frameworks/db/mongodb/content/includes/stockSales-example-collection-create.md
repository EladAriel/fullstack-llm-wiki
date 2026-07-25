---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/stockSales-example-collection-create.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```javascript
db.stockSales.insertMany( [
   { _id: 0, symbol: "MDB", saleTimestamp: Timestamp(1622731060, 1) },
   { _id: 1, symbol: "MDB", saleTimestamp: Timestamp(1622731060, 2) },
   { _id: 2, symbol: "MSFT", saleTimestamp: Timestamp(1714124193, 1) },
   { _id: 3, symbol: "MSFT", saleTimestamp: Timestamp(1714124193, 2) },
   { _id: 4, symbol: "MSFT", saleTimestamp: Timestamp(1714124193, 3) }
] )
```
