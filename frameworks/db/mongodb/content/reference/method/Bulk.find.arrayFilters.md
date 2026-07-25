---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.arrayFilters.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================================

# Bulk.find.arrayFilters() (mongosh method)

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

```javascript
var bulk = db.coll.initializeUnorderedBulkOp();
bulk.find({}).arrayFilters( [ { "elem.grade": { $gt: 85 } } ] ).updateOne( { $set: { "grades.$[elem].mean" : 70 } } );
bulk.execute();
```

> **Seealso:** - :method:`db.collection.initializeUnorderedBulkOp()`
- :method:`db.collection.initializeOrderedBulkOp()`
- :method:`Bulk.find.update()`
- :method:`Bulk.find.updateOne()`
- :method:`Bulk.execute()`
- `All Bulk Methods <bulk-methods>`
