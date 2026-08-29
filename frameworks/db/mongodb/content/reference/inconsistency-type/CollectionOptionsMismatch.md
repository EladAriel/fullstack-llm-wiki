---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CollectionOptionsMismatch.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.855825Z"
---
# CollectionOptionsMismatch

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. |incon-type| replace:: ``CollectionOptionsMismatch``

## Description

**data:** CollectionOptionsMismatch

   .. include:: /includes/inconsistency-type/CollectionOptionsMismatch.rst

## Format

.. code-block:: json

   {
      type: "CollectionOptionsMismatch",
      description: "<string>",
      details: {
         namespace: "<string>",
         options: <array>
      }
   }

|incon-type| inconsistency documents contain these fields:

.. list-table::
   :widths: 30 25 45
   :header-rows: 1

   * - Field
     - Type
     - Description

   * - ``type``
     - string
     - .. include:: /includes/inconsistency-type/type.rst

   * - ``description``
     - string
     - .. include:: /includes/inconsistency-type/descr.rst

   * - ``details``
     - document
     - .. include:: /includes/inconsistency-type/details.rst

   * - ``details.namespace``
     - string
     - .. include:: /includes/inconsistency-type/details.namespace.rst

   * - ``details.options``
     - array
     - .. include:: /includes/inconsistency-type/details.options.rst

## Example

**include:** /includes/inconsistency-type/example.rst

.. code-block:: json
   :emphasize-lines: 6-15
   :copyable: false

   {
      cursor: {
         id: Long("0"),
         ns: "test.$cmd.aggregate",
         firstBatch: [
            {
               type: "CollectionOptionsMismatch",
               description: "Found collection with mismatching options across shards and/or config server",
               details: {
                  namespace: "test.authors",
                  options: [ 
                     { "options": { "capped": true }, "shards": [ "shard0" ] },
                     { "options": { "capped": false }, "shards": [ "shard1", "config" ] }
                  ]
               }
            }
         ],
      },
      ok: 1
   }