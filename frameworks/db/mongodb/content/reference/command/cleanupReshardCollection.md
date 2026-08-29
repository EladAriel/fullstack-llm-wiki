---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/cleanupReshardCollection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.065403Z"
---
# cleanupReshardCollection (database command)

**meta:** :description: Clean up metadata from a failed resharding operation using the `cleanupReshardCollection` command after a primary failover.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** cleanupReshardCollection

   .. versionadded:: 5.0

   The :dbcommand:`cleanupReshardCollection` command cleans up metadata
   of a failed :ref:`resharding operation <sharding-resharding>`. You
   only need to run this command if a primary failover occurred while you
   ran a resharding operation.

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
       cleanupReshardCollection: "<database>.<collection>"
     }
  )

## Example

### Clean up a Failed Resharding Operation

The following example cleans up metadata of a failed :ref:`resharding
operation <sharding-resharding>` on the ``sales.orders`` collection:

.. code-block:: javascript

   db.adminCommand({
     cleanupReshardCollection: "sales.orders"
   })

**seealso:** :ref:`sharding-resharding`