---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/array-sort-example-setup.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When MongoDB sorts documents by an array-value field, the `sort key` depends on whether the sort is ascending or descending:

- In an ascending sort, the sort key is the lowest value in the array.
- In a descending sort, the sort key is the highest value in the array.
The query filter does not affect sort key selection.

For example, create a `shoes` collection with these documents:

```javascript
db.shoes.insertMany( [
   { _id: 'A', sizes: [ 7, 11 ] }, 
   { _id: 'B', sizes: [ 8, 9, 10 ] }
] )
```
