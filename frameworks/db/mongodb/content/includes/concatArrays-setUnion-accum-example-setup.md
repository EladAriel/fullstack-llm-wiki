---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/concatArrays-setUnion-accum-example-setup.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
