---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/commitTransaction.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# commitTransaction (database command)

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
     commitTransaction: 1, 
     txnNumber: <long>,
     writeConcern: <document>,
     autocommit: false,
     comment: <any>
   }
)
```

## Behavior

### Write Concern

When committing the transaction, the session uses the `write concern </reference/write-concern>` specified at the transaction start. See :method:`Session.startTransaction()`.

If you commit using the :writeconcern:`"w: 1" <\<number\>>` write concern, your transaction can be `rolled back if there is a failover. </core/replica-set-rollbacks>`.

### Atomicity

When a transaction commits, all data changes made in the transaction are saved and visible outside the transaction. That is, a transaction will not commit some of its changes while rolling back others.

.. include:: /includes/extracts/transactions-committed-visibility.rst
