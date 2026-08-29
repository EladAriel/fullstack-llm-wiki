---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CollectionUUIDMismatch.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.855479Z"
---
# CollectionUUIDMismatch

**meta:** :description: Identify and understand `CollectionUUIDMismatch` inconsistencies in MongoDB sharded clusters, including their format and how to detect them.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. |incon-type| replace:: ``CollectionUUIDMismatch``

# Description

**data:** CollectionUUIDMismatch

   .. include:: /includes/inconsistency-type/CollectionUUIDMismatch

# Format

.. code-block:: json

   {
      type: "CollectionUUIDMismatch",
      description: "<string>",
      details: {
         namespace: "<string>",
         shard: "<string>",
         localUUID: UUID("<uuid>"),
         uuid: UUID("<uuid>")
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

   * - ``details.shard``
     - string
     - .. include:: /includes/inconsistency-type/details.shard

   * - ``details.localUUID``
     - UUID
     - The UUID registered locally on the shard. 
     
   * - ``details.uuid``
     - UUID
     - The UUID of the collection found in the :data:`config.collections` 
       cluster catalog.

# Example

**include:** /includes/inconsistency-type/example

.. code-block:: json
   :emphasize-lines: 6-15
   :copyable: false

   {
      cursor: {
         id: Long("0"),
         ns: "test.$cmd.aggregate",
         firstBatch: [
            {
               type: "CollectionUUIIDMismatch",
               description: "Found collection on non primary shard with mismatching UUID",
               details: {
                  namespace: "test.authors",
                  shard: "shard02",
                  localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
                  uuid: new UUID("a3153e8a-3544-43ec-928f-37f72b48dee9")
               }
            }
         ],
      },
      ok: 1
   }