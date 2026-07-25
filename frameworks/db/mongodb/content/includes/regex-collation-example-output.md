---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/regex-collation-example-output.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Both operations return the following:

```javascript
{ "_id" : 1, "category" : "café", "resultObject" : null }
{ "_id" : 2, "category" : "cafe", "resultObject" : { "match" : "cafe", "idx" : 0, "captures" : [ ] } }
{ "_id" : 3, "category" : "cafE", "resultObject" : null }
```

Because the query ignores the collation, it requires an exact match on the `category string (including case and accent marks), meaning only document id: 2` is matched.
