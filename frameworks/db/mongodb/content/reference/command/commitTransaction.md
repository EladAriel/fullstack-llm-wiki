---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/commitTransaction.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.066093Z"
---
# commitTransaction (database command)

**meta:** :description: Execute the `commitTransaction` command to save changes from a multi-document transaction and end the transaction in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** commitTransaction

   Saves the changes made by the operations in the :doc:`multi-document
   transaction </core/transactions>` and ends the transaction. 

   .. |method| replace:: :method:`Session.commitTransaction` and
      :method:`Session.withTransaction`
      helper methods
   .. include:: /includes/fact-dbcommand-tip

   To run the :dbcommand:`commitTransaction`, the command must be run
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
        commitTransaction: 1, 
        txnNumber: <long>,
        writeConcern: <document>,
        autocommit: false,
        comment: <any>
      }
   )

## Behavior

### Write Concern

When committing the transaction, the session uses the :doc:`write
concern </reference/write-concern>` specified at the transaction start.
See :method:`Session.startTransaction()`.

If you commit using the :writeconcern:`"w: 1" <\<number\>>` write
concern, your transaction can be :doc:`rolled back if there is a
failover. </core/replica-set-rollbacks>`.

### Atomicity

When a transaction commits, all data changes made in the transaction
are saved and visible outside the transaction. That is, a transaction
will not commit some of its changes while rolling back others.

**include:** /includes/extracts/transactions-committed-visibility.rst