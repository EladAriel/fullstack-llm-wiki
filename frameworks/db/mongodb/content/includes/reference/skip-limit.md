---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/reference/skip-limit.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When you chain :method:`~cursor.skip()` and :method:`~cursor.limit()`, the method chaining order does not affect the results. The server always applies the skip operation based on the sort order before it applies the limit on how many documents to return.

The following code example shows different chaining orders for :method:`~cursor.skip()` and :method:`~cursor.limit()` that always produce the same query results for the same data set:

```javascript
db.myColl.find().sort({_id: 1}).skip(3).limit(6);

db.myColl.find().sort({_id: 1}).limit(6).skip(3);
```
