---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.abortMoveCollection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.886877Z"
---
# sh.abortMoveCollection() (mongosh method)

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.abortMoveCollection(namespace)

   .. include:: /includes/command/abortMoveCollection.rst

   This method must run on the ``admin`` database.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

.. code-block:: javascript

   sh.abortMoveCollection( "<namespace>.<collection>" )

## Parameters

.. list-table::
   :header-rows: 1
   :widths: 20 10 10 60

   * - Field
     - Type
     - Necessity
     - Description

   * - ``coll``
     - string
     - Required
     - Specifies the database and collection to stop moving.

## Examples

**include:** /includes/amc-example-intro.rst

.. code-block:: javascript

   sh.abortMoveCollection( "sales.us_accounts" )

## Learn More

- :dbcommand:`abortMoveCollection`
- :ref:`task-stop-moving-a-collection`