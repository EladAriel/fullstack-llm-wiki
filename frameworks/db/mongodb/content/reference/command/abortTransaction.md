---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortTransaction.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.056372Z"
---
# abortTransaction (database command)

**meta:** :description: Terminate a multi-document transaction using the abortTransaction command, which rolls back all changes made during the transaction.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** abortTransaction

   Terminates the :doc:`multi-document transaction
   </core/transactions>` and rolls back any data changes made by the
   operations within the transaction. That is, the transaction ends
   without saving any of the changes made by the operations in the
   transaction.

   .. |method| replace:: :method:`Session.abortTransaction`
      helper method
   .. include:: /includes/fact-dbcommand-tip

   To run the :dbcommand:`abortTransaction`, the command must be run
   against the ``admin`` database and run within a
   :method:`Session`.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

.. code-block:: javascript

   db.adminCommand(
      {      
        abortTransaction: 1, 
        txnNumber: <long>,
        writeConcern: <document>,
        autocommit: false,
        comment: <any>
      }
   )

## Behavior

### Atomicity

When a transaction aborts, all data changes made by the writes in the
transaction are discarded without ever becoming visible and the
transaction ends.

### Security

If running with :ref:`auditing <auditing>`, operations in an
aborted transaction are still audited.
  