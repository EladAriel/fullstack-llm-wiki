---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/skip-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you chain :method:`~cursor.skip()` and :method:`~cursor.limit()`, the method chaining order does not affect the results. The server always applies the skip operation based on the sort order before it applies the limit on how many documents to return.

The following code example shows different chaining orders for :method:`~cursor.skip()` and :method:`~cursor.limit()` that always produce the same query results for the same data set:

```javascript
db.myColl.find().sort({_id: 1}).skip(3).limit(6);

db.myColl.find().sort({_id: 1}).limit(6).skip(3);
```
