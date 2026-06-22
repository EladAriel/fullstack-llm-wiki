---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortTransaction.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# abortTransaction (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {      
     abortTransaction: 1, 
     txnNumber: <long>,
     writeConcern: <document>,
     autocommit: false,
     comment: <any>
   }
)
```

## Behavior

### Atomicity

When a transaction aborts, all data changes made by the writes in the transaction are discarded without ever becoming visible and the transaction ends.

### Security

If running with `auditing <auditing>`, operations in an aborted transaction are still audited.
