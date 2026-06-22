---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/concatArrays-setUnion-accum-example-setup.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Create a collection named `sales` with the following documents:

```javascript
db.sales.insertMany( [
   {
     _id: 1,
     items: [ "laptop", "tablet" ],
     location: "NYC"
   },
   {
     _id: 2,
     items: [ "phone", "tablet" ],
     location: "NYC"
   },
   {
     _id: 3,
     location: "NYC"
   },
   {
     _id: 4,
     items: [ "desktop", { "accessories": [ "mouse", "keyboard"] } ],
     location: "NYC"
   }
] )
```
