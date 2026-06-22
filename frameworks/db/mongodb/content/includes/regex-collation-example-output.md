---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/regex-collation-example-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Both operations return the following:

```javascript
{ "_id" : 1, "category" : "café", "resultObject" : null }
{ "_id" : 2, "category" : "cafe", "resultObject" : { "match" : "cafe", "idx" : 0, "captures" : [ ] } }
{ "_id" : 3, "category" : "cafE", "resultObject" : null }
```

Because the query ignores the collation, it requires an exact match on the `category string (including case and accent marks), meaning only document id: 2` is matched.
