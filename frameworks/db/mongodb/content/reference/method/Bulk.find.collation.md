---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.collation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Bulk.find.collation() (mongosh method)

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

.. include:: /includes/collation-data-setup.rst

The following example initializes a :method:`Bulk()` operations builder for the `restaurants` collection and specifies a collation for the find filter.

The operation specifies a collation with `strength: 1`, which means the collation ignores differences between case and letter variants. As a result, even though there is only one document that has an exact match as the string specified in the filter (`cafe`), the operation matches and updates all documents in the collection.

After the bulk operation completes, the collection contains these documents:

```javascript
[
   { _id: 1, category: 'café', status: 'closed', points: '0' },
   { _id: 2, category: 'cafe', status: 'closed', points: '0' },
   { _id: 3, category: 'cafE', status: 'closed', points: '0' }
]
```

## Learn More

- :method:`db.collection.initializeUnorderedBulkOp()`
- :method:`db.collection.initializeOrderedBulkOp()`
- :method:`Bulk.find()`
- :method:`Bulk.find.updateOne()`
- :method:`Bulk.execute()`
- `All Bulk Methods <bulk-methods>`
