---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/abortRewriteCollection.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.048586Z"
---
# abortRewriteCollection (database command)

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

## Definition

**dbcommand:** abortRewriteCollection

   .. include:: /includes/command/abortRewriteCollection

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst
 
## Syntax

.. code-block:: javascript

   db.adminCommand( {
      abortRewriteCollection: "<database>.<collection>"
   } )

## Command Fields

The command takes the following field:

.. list-table::
   :header-rows: 1
   :widths: 30 10 10 50

   * - Field
     - Type
     - Necessity
     - Description

   * - ``abortRewriteCollection``
     - string
     - Required
     - Specifies the database and collection to stop rewriting.

## Access Control

The ``abortRewriteCollection`` command requires the
:authaction:`rewriteCollection` privilege action on the cluster
or on the database and collection on which you want to stop the
rewrite.

This privilege action is also available to users with the
following roles:

- :authrole:`enableSharding`

- :authrole:`clusterManager`

## Examples

Consider the following example of a collection rewrite:

.. code-block:: javascript

   db.adminCommand( {
     rewriteCollection: "sales.orders"
   } )

To stop this rewrite, pass the database and collection name to
the ``abortRewriteCollection`` command:

.. code-block:: javascript

   db.adminCommand( {
      abortRewriteCollection: "sales.orders"
   } )

## Learn More

- :ref:`sharding-introduction`

- :dbcommand:`rewriteCollection`

- :dbcommand:`reshardCollection`

- :dbcommand:`abortReshardCollection`
