---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-indexes-considerations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- Wildcard indexes omit the `_id` field by default. To include the
`_id` field in a wildcard index, you must explicitly include it in the `wildcardProjection` document.

```javascript
  db.salesData.createIndex(
     { "$**" : 1 },
     { "wildcardProjection" :
        { "_id": 1, "customers.lastName": 1, "customers.FirstName": 1, }
     }
  )
```

- You can create more than one wildcard index on a collection.
- A wildcard index may cover the same fields as other indexes in the
collection.

- Wildcard indexes are `sparse <index-type-sparse>`. They only
include entries for documents that contain the indexed field.

The document is not indexed if all of the fields in the compound wildcard index are missing.
