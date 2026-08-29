---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CollectionAuxiliaryMetadataMismatch.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.860037Z"
---
# CollectionAuxiliaryMetadataMismatch

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. |incon-type| replace:: ``CollectionAuxiliaryMetadataMismatch``

## Description

**data:** CollectionAuxiliaryMetadataMismatch

   .. include:: /includes/inconsistency-type/CollectionAuxiliaryMetadataMismatch.rst

## Format

.. code-block:: json

   {
      type: "CollectionAuxiliaryMetadataMismatch",
      description: "<string>",
      details: {
         namespace: "<string>",
         collectionMetadata: <array>
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

   * - ``details.collectionMetadata``
     - array
     - .. include:: /includes/inconsistency-type/details.collectionMetadata.rst

## Example

**include:** /includes/inconsistency-type/example.rst

.. code-block:: json
   :emphasize-lines: 6-16
   :copyable: false

   {
      cursor: {
         id: Long("0"),
         ns: "test.$cmd.aggregate",
         firstBatch: [
            {
               type: "CollectionAuxiliaryMetadataMismatch",
               description: "Found collection with mismatching auxiliary metadata across shards and/or config server",
               details: {
                  namespace: "test.authors",
                  collectionMetadata: [ 
                     { "md": { "exampleField": 123 }, "shards": [ "shard0" ] },
                     { "md": { "exampleField": 321 }, "shards": [ "shard1" ] }
                  ]
               }
            }
         ],
      },
      ok: 1
   }