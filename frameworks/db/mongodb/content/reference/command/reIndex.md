---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/reIndex.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.056078Z"
---
# reIndex (database command)

**meta:** :description: Run the `reIndex` command to drop and recreate all indexes on a collection, available only on standalone instances.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** reIndex

   .. deprecated:: 6.0
   
   Attempting to run the :dbcommand:`reIndex` command writes a warning 
   message to the log.

   .. |method| replace:: :method:`db.collection.reIndex` helper method
   .. include:: /includes/fact-dbcommand-tip

   The :dbcommand:`reIndex` command drops all indexes on a
   collection and recreates them. This operation may be expensive for
   collections that have a large amount of data and/or a large number
   of indexes. 

   .. warning::

      - :dbcommand:`reIndex` may only be run on :term:`standalone` 
        instances. 
      - For most users, the :dbcommand:`reIndex` command is unnecessary.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst

**include:** /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

.. code-block:: javascript

   db.runCommand(
      { 
        reIndex: <collection> 
      }
   )

## Command Fields

The command takes the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 80
 
   * - Field
     - Description
 
   * - reIndex
     - The name of the collection to reindex.
 

## Behavior

For MongoDB 5.0 or later, :dbcommand:`reIndex` may only be run on 
:term:`standalone` instances.

### Resource Locking

:dbcommand:`reIndex` obtains an exclusive (W) lock on the collection and blocks 
other operations on the collection until it completes.

For more information on locking in MongoDB, see :doc:`/faq/concurrency`.

**see:** :doc:`/core/index-creation` for more information on the
   behavior of indexing operations in MongoDB.