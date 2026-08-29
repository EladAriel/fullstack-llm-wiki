---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/dropDatabase.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.877565Z"
---
.. _change-event-dropDatabase:

.. _change-streams-dropDatabase-event:

# dropDatabase Event

**meta:** :description: Understand the `dropDatabase` event in MongoDB, which occurs when a database is dropped, including its fields and example structure.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

.. |idref| replace:: ce-dropDatabase


## Synopsis

**data:** dropDatabase

   A ``dropDatabase`` event occurs when a database is dropped. 

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


   * - ``lsid``
     - document
     - .. include:: /includes/change-stream/lsid

   * - ``ns``
     - document
     - .. include:: /includes/change-stream/ns

   * - ``ns.db``
     - string
     - .. include:: /includes/change-stream/ns.db

   * - ``operationType``
     - string
     - .. include:: /includes/change-stream/operationType

       Returns a value of ``dropDatabase`` for these change events.

   * - ``txnNumber``
     - NumberLong
     - .. include:: /includes/change-stream/txnNumber

   * - ``wallTime``
     - :term:`ISODate`
     - .. include:: /includes/change-stream/wallTime

## Example

The following example illustrates a ``dropDatabase`` event:

.. code-block:: json
   :copyable: false

   {
      "_id": { <Resume Token> },
      "operationType": "dropDatabase",
      "clusterTime": <Timestamp>,
      "wallTime": <ISODate>,
      "ns": {
         "db": "engineering"
      }
   }

A :dbcommand:`dropDatabase` command generates a
:ref:`drop event <change-streams-drop-event>` for each collection in
the database before generating a ``dropDatabase`` event for the database.

A ``dropDatabase`` event leads to an :data:`invalidate` event for 
change streams opened against its own ``ns.db`` database.

