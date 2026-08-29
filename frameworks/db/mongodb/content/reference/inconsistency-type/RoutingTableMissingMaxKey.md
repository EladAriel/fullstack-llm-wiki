---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/RoutingTableMissingMaxKey.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.857817Z"
---
# RoutingTableMissingMaxKey

**meta:** :description: Understand the `RoutingTableMissingMaxKey` inconsistency in MongoDB, where a sharding range gap exists because the routing table does not reach the maximum key.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. |incon-type| replace:: ``RoutingTableMissingMaxKey``

# Description

**data:** RoutingTableMissingMaxKey

   .. include:: /includes/inconsistency-type/RoutingTableMissingMaxKey

# Format

.. code-block:: json
   :copyable: false

   {
      type: "RoutingTableMissingMaxKey",
      description: "<string>",
      details: {
         namespace: "<string>",
         collectionUUID: <string>,
         maxKeyObj: { <document> },
         globalMax: { <document> }
      }
   }


|incon-type| inconsistency documents contain the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 20 60

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
     - .. include:: /includes/inconsistency-type/details.collectionUUID

   * - ``details.maxKeyObj``
     - document
     - The max key used by the collection.

   * - ``details.globalMax``
     - document
     - The expected max key of the collection.

# Example

**include:** /includes/inconsistency-type/example

.. code-block:: json
   :emphasize-lines: 6-19
   :copyable: false

   {
      cursor: {
         id: Long("0"),
         ns: "test.$cmd.aggregate",
         firstBatch: [
            {
               type: "RoutingTableMissingMaxKey",
               description: "Routing table has a gap because last chunk boundary does not reach MaxKey",
               details: {
                  namespace: "test.authors",
                  collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
                  maxKeyObj: { 
                     x: 0 
                  },
                  globalMax: { 
                     x: MaxKey 
                  }
               }
            }
         ],
      },
      ok: 1
   }