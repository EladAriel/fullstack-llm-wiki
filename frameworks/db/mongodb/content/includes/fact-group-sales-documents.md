---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-group-sales-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In :binary:`~bin.mongosh`, create a sample collection named `sales` with the following documents:

```javascript
db.sales.insertMany([
  { "_id" : 1, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("2"), "date" : ISODate("2014-03-01T08:00:00Z") },
  { "_id" : 2, "item" : "jkl", "price" : Decimal128("20"), "quantity" : Int32("1"), "date" : ISODate("2014-03-01T09:00:00Z") },
  { "_id" : 3, "item" : "xyz", "price" : Decimal128("5"), "quantity" : Int32( "10"), "date" : ISODate("2014-03-15T09:00:00Z") },
  { "_id" : 4, "item" : "xyz", "price" : Decimal128("5"), "quantity" :  Int32("20") , "date" : ISODate("2014-04-04T11:21:39.736Z") },
  { "_id" : 5, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("10") , "date" : ISODate("2014-04-04T21:23:13.331Z") },
  { "_id" : 6, "item" : "def", "price" : Decimal128("7.5"), "quantity": Int32("5" ) , "date" : ISODate("2015-06-04T05:08:13Z") },
  { "_id" : 7, "item" : "def", "price" : Decimal128("7.5"), "quantity": Int32("10") , "date" : ISODate("2015-09-10T08:43:00Z") },
  { "_id" : 8, "item" : "abc", "price" : Decimal128("10"), "quantity" : Int32("5" ) , "date" : ISODate("2016-02-06T20:20:13Z") },
])
```
