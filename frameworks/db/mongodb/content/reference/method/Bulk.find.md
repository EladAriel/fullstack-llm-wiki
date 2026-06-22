---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Bulk.find.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# Bulk.find() (mongosh method)

.. include:: /includes/fact-bulkwrite.rst

## Description

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

## Example

The following example initializes a :method:`Bulk()` operations builder for the `items` collection and adds a remove operation and an update operation to the list of operations. The remove operation and the update operation use the :method:`Bulk.find()` method to specify a condition for their respective actions:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "D" } ).delete();
bulk.find( { status: "P" } ).update( { $set: { points: 0 } } )
bulk.execute();
```

> **Seealso:** - :method:`db.collection.initializeUnorderedBulkOp()`
- :method:`db.collection.initializeOrderedBulkOp()`
- :method:`Bulk.execute()`
