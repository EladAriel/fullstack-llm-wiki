---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/drop.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.095516Z"
---
# drop (database command)

**meta:** :description: Remove an entire collection from a database using the `drop` command, which also deletes associated indexes and handles in-progress index builds.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** drop

   The :dbcommand:`drop` command removes an entire collection from a
   database. 

   .. |method| replace:: :method:`~db.collection.drop` helper method
   .. include:: /includes/fact-dbcommand-tip

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

                
## Syntax

The command has following syntax:

.. code-block:: javascript

   db.runCommand(
      { 
        drop: <collection_name>, 
        writeConcern: <document>, 
        comment: <any> 
      }
   )

## Command Fields

The command takes the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 80
 
   * - Field
     - Description
 
   * - ``drop``
     - The name of the collection to drop.
 
   * - ``writeConcern``
 
     - Optional. A document expressing the :doc:`write concern
       </reference/write-concern>` of the :dbcommand:`drop` command.
       Omit to use the default write concern.
 
       .. include:: /includes/extracts/mongos-operations-wc-drop.rst
 
   * - ``comment``
 
     - .. include:: /includes/extracts/comment-content.rst

:binary:`~bin.mongosh` provides the equivalent helper method
:method:`db.collection.drop()`.

## Behavior

- Starting in MongoDB 5.0, the :dbcommand:`drop` command and the
  :method:`db.collection.drop()` method will raise an error if passed an
  unrecognized parameter.

- This command also removes any indexes associated with the dropped
  collection.

- .. include:: /includes/extracts/4.4-changes-drop-in-progress-indexes.rst

- The :dbcommand:`drop` command and its helper
  :method:`db.collection.drop()` create an :ref:`change-event-invalidate`
  for any :doc:`/changeStreams` opened on the dropped collection.

- .. include:: /includes/extracts/zoned-sharding-drop-collection-change.rst

- .. include:: /includes/extracts/5.0-changes-drop-sharding.rst

### Resource Locking

**include:** /includes/extracts/drop-resource-lock.rst