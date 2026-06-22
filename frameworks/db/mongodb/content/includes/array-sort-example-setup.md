---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/array-sort-example-setup.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
