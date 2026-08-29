---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortReshardCollection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.018218Z"
---
# abortReshardCollection (database command)

**meta:** :description: Abort a resharding operation in MongoDB using the `abortReshardCollection` command before the commit phase.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** abortReshardCollection

   .. versionadded:: 5.0

   During a :ref:`resharding operation <sharding-resharding>`, you can
   abort the operation with the :dbcommand:`abortReshardCollection`
   command.

   You can abort a :ref:`resharding operation <sharding-resharding>` at
   any point until the :ref:`commit phase
   <resharding-commit-phase-command>`. If the :ref:`resharding operation
   <sharding-resharding>` has reached the :ref:`commit phase
   <resharding-commit-phase-command>` before you run the
   :dbcommand:`abortReshardCollection` command, the command returns an
   error.


   .. |method| replace:: :method:`sh.abortReshardCollection` 
      helper method
   .. include:: /includes/fact-dbcommand-tip

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
        abortReshardCollection: "<database>.<collection>"
      } 
   )

## Example

### Abort a Resharding Operation

The following example aborts a running :ref:`resharding operation
<sharding-resharding>` on the ``sales.orders`` collection:

.. code-block:: javascript

   db.adminCommand({
     abortReshardCollection: "sales.orders"
   })

**seealso:** :ref:`sharding-resharding`