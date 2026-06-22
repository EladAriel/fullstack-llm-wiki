---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-roles-privileges-multiple-collections.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you specify the `privileges` array, you can specify `privileges <privileges>` to apply to multiple collections in a database or to an entire database.

The following syntax specifies privileges on multiple collections in the `products` database.

```javascript
privileges: [
     {
     resource: { db: 'products', collection: 'coll1' },
     actions: [ 'bypassDocumentValidation' ]
     },
     {
     resource: { db: 'products', collection: 'coll2' },
     actions: [ 'bypassDocumentValidation' ]
     }     
]
```

The following syntax specifies privileges on all collections in the `products` database.

```javascript
privileges: [
     {
     resource: { db: 'products', collection: '' },
     actions: [ 'bypassDocumentValidation' ]
     }
]
```
