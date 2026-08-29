---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CorruptedChunkShardKey.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.856171Z"
---
# CorruptedChunkShardKey

**meta:** :description: Identify and understand `CorruptedChunkShardKey` inconsistencies in MongoDB sharding metadata, including their format and example usage.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

.. |incon-type| replace:: ``CorruptedChunkShardKey``

# Description

**data:** CorruptedChunkShardKey

   .. include:: /includes/inconsistency-type/CorruptedChunkShardKey

# Format

.. code-block:: json

   {
      type: "CorruptedChunkShardKey",
      description: "<string>",
      details: {
         namespace: "<string>",
         collectionUUID: UUID("<uuid>"),
         chunk: <chunk>,
         shardKeyPattern: <pattern>
      }
   }

|incon-type| inconsistency documents contain the following fields:

.. list-table::
   :header-rows: 1
   :widths: 30 25 45

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
     - UUID of the collection with the corrupted chunk shard key.

   * - ``details.chunk``
     - document
     - Chunk with the corrupted shard key.

   * - ``details.shardKeyPattern``
     - document
     - .. include:: /includes/inconsistency-type/details.shardKeyPattern

# Example

**include:** /includes/inconsistency-type/example

.. code-block:: json
   :emphasize-lines: 6-35
   :copyable: false

   { 
      cursor: {
         id: Long("0"),
         ns: "test.$cmd.aggregate",
         firstBatch: [ 
            {
               type: "CorruptedChunkShardKey",
               description: "Found chunk with a shard key pattern violation",
               details: {
                  namespace: "test.authors",
                  collectionUUID : new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
                  chunk: { 
                     _id: ObjectId("64ddd81656be208c6685da1b"),
                     uuid: new UUID("de934e0a-74d2-412b-9bb8-409abe9754e3"),
                     min: { 
                        y: 0 
                     }, 
                     max: { 
                        x: MaxKey 
                     }, 
                     shard: "shard0000", 
                     lastmod: Timestamp(1, 0),
                     onCurrentShardSince: Timestamp(1, 0), 
                     history: [ 
                        { 
                           validAfter: Timestamp(1, 0), 
                           shard: "shard0000" 
                        } 
                     ]
                  },
                  shardKeyPattern: { 
                     x: 1 
                  }
               }
            }
         ],
      },
      ok: 1
   }