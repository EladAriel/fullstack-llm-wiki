---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.setCausalConsistency.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Mongo.setCausalConsistency() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Example

The following :binary:`~bin.mongosh` operation enables causal consistency on the :method:`Mongo` connection object associated with :binary:`~bin.mongosh`'s global `db` variable:

```javascript
db.getMongo().setCausalConsistency();
```

> **Seealso:** - :method:`db.getMongo()`
