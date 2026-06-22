---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/lt-lte-sample-data.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```javascript
db.inventory.insertMany( [
   { _id : 1, item : "abc1", description: "product 1", qty: 300 },
   { _id : 2, item : "abc2", description: "product 2", qty: 200 },
   { _id : 3, item : "xyz1", description: "product 3", qty: 250 },
   { _id : 4, item : "VWZ1", description: "product 4", qty: 300 },
   { _id : 5, item : "VWZ2", description: "product 5", qty: 180 }
] )
```
