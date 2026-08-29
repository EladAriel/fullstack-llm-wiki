---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortMoveCollection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.048870Z"
---
# abortMoveCollection (database command)

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** abortMoveCollection

   .. include:: /includes/command/abortMoveCollection.rst

   This command must run on the ``admin`` database.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.txt

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

.. code-block:: javascript

   db.adminCommand( { 
      abortMoveCollection: "<database>.<collection>" 
   } )

## Command Fields

.. list-table::
   :header-rows: 1
   :widths: 20 10 10 60

   * - Field
     - Type
     - Necessity
     - Description

   * - ``abortMoveCollection``
     - string
     - Required
     - Specifies the database and collection to stop moving.

## Examples

**include:** /includes/amc-example-intro.rst

.. code-block:: javascript

   db.adminCommand( { 
      abortMoveCollection: "sales.us_accounts" 
   } )

## Learn More

- :method:`sh.abortMoveCollection`
- :ref:`task-stop-moving-a-collection`