---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/MissingShardKeyIndex.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.860331Z"
---
# MissingShardKeyIndex

**meta:** :description: Identify and resolve the MissingShardKeyIndex inconsistency type, which occurs when a sharded collection does not have an index that supports its shard key.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. |incon-type| replace:: ``MissingShardKeyIndex``

# Description

**data:** MissingShardKeyIndex

   .. include:: /includes/inconsistency-type/MissingShardKeyIndex

# Format

.. code-block:: json
   :copyable: false

   {
      type: "MissingShardKeyIndex",
      description: "<string>",
      details: {
         namespace: "<string>",
         shard: "<string>",
         shardKey: { <document> }
      }
   }

|incon-type| inconsistency documents contain the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 15 65 

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

   * - ``details.shardKey``
     - document
     - The shard key that requires an index. 

# Example

**include:** /includes/inconsistency-type/example

.. code-block:: json
   :emphasize-lines: 6-16
   :copyable: false

   {
      cursor: {
         id: Long("0"),
         ns: "test.$cmd.aggregate",
         firstBatch: [
            {
               type: "MissingShardKeyIndex",
               description: "Found sharded collection without a shard key index",
               details: {
                  namespace: "test.authors",
                  shard: "shard-rs0",
                  shardKey: { 
                     skey: 1
                  }
               }
            }
         ],
      },
      ok: 1
   }