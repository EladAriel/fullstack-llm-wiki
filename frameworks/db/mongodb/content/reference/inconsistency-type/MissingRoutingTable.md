---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/MissingRoutingTable.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.858115Z"
---
# MissingRoutingTable

**meta:** :description: Identify and understand the `MissingRoutingTable` inconsistency in sharded collections, including its format and example usage.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. |incon-type| replace:: ``MissingRoutingTable``

# Description

**data:** MissingRoutingTable

   .. include:: /includes/inconsistency-type/MissingRoutingTable

# Format

.. code-block:: json

   {
      type: "MissingRoutingTable",
      description: "<string>",
      details: {
         namespace: "<string>",
         collectionUUID <uuid>
      }
   }

|incon-type| inconsistency documents contain the following fields:

.. list-table::
   :widths: 30 25 45
   :header-rows: 1

   * - Field
     - Type
     - Description

   * - ``type``
     - string
     - .. include:: /includes/inconsistency-type/type

   * - ``description``
     - string
     - .. include:: /includes/inconsistency-type/descr

   * - ``details``
     - document
     - .. include:: /includes/inconsistency-type/details

   * - ``details.namespace``
     - string
     - .. include:: /includes/inconsistency-type/details.namespace

   * - ``details.collectionUUID``
     - UUID
     - UUID of the collection without the routing table.

# Example

**include:** /includes/inconsistency-type/example

.. code-block:: json
   :emphasize-lines: 6-13
   :copyable: false

   {
      cursor: {
         id: Long("0"),
         ns: "test.$cmd.aggregate",
         firstBatch: [
            {
               type: "MissingRoutingTable",
               description: "There is a sharded collection without routing table",
               details: {
                  namespace: "test.authors",
                  collectionUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4")
               }
            }
         ],
      },
      ok: 1
   }