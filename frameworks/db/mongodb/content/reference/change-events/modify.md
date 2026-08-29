---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/modify.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.875458Z"
---
.. _change-event-modify:

# ``modify`` Event

**meta:** :description: Understand the modify event in MongoDB change streams, which occurs when collection options are altered, requiring the showExpandedEvents option to be enabled.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

.. |idref| replace:: ce-modify

## Summary

**data:** modify

   .. versionadded:: 6.0

   A ``modify`` event occurs when a collection is modified, such as when the
   :dbcommand:`collMod` command adds or remove options from a collection or 
   view. This event is received only if the change stream has the 
   :ref:`showExpandedEvents <change-streams-expanded-events>` option 
   set to ``true``.

   .. note:: Disambiguation

      To learn more about events that occur when individual documents are
      updated, see the :data:`update` event.


## Description

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

   * - Field
     - Type
     - Description

   * - ``_id``
     - Document
     - .. include:: /includes/change-stream/id

   * - ``clusterTime``
     - Timestamp
     - .. include:: /includes/change-stream/clusterTime

   * - ``collectionUUID``
     - UUID
     - .. include:: /includes/change-stream/collectionUUID-views

   * - ``lsid``
     - document
     - .. include:: /includes/change-stream/lsid

   * - ``ns``
     -  document
     - .. include:: /includes/change-stream/ns

   * - ``ns.db``
     - string
     - .. include:: /includes/change-stream/ns.db

   * - ``ns.coll``
     - string
     - .. include:: /includes/change-stream/ns.coll

   * - ``operationDescription``
     - document
     - .. include:: /includes/change-stream/operationDescription

   * - | ``operationDescription.``
       | ``index``
     - document
     - .. include:: /includes/change-stream/od-index

   * - | ``operationDescription.``
       | ``indexes``
     - array
     - An array of documents listing the indexes that were changed 
       by the operation.


   * - ``operationType``
     - string
     - .. include:: /includes/change-stream/operationType

       Returns a value of ``modify`` for these change events.

   * - ``stateBeforeChange``
     - document
     - .. include:: /includes/change-stream/stateBeforeChange

   * - | ``stateBeforeChange.``
       | ``collectionOptions``
     - document
     - .. include:: /includes/change-stream/stateBeforeChange.collectionOptions

   * - | ``stateBeforeChange.``
       | ``indexOptions``
     - document
     - .. include:: /includes/change-stream/stateBeforeChange.indexOptions

   * - ``txnNumber``
     - NumberLong
     - .. include:: /includes/change-stream/txnNumber

   * - ``wallTime``
     - :term:`ISODate`
     - .. include:: /includes/change-stream/wallTime


## Example

The following example shows a ``modify`` event:

.. code-block:: json
   :copyable: false

   {
      "_id": { <ResumeToken> },
      "operationType": "modify",
      "clusterTime": Timestamp({ t: 1654878543, i: 1 }),
      "collectionUUID": UUID("47d6baac-eeaa-488b-98ae-893f3abaaf25"),
      "wallTime": ISODate("2022-06-10T16:29:03.704Z"),
      "ns": {
         "db": "test",
         "coll": "authors" },
      "operationDescription": {
         "index": {
            "name": "age_1",
            "hidden": true
         }
      },
      "stateBeforeChange": {
         "collectionOptions": { 
             "uuid": UUID("47d6baac-eeaa-488b-98ae-893f3abaaf25") 
         },
         "indexOptions": {
            "hidden": false
         }
      }
   }
