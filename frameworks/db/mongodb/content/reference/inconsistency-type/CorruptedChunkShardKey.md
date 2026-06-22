---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CorruptedChunkShardKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

###################### CorruptedChunkShardKey ######################

# Description

# Format

```json
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
```

|incon-type| inconsistency documents contain the following fields:

# Example

.. include:: /includes/inconsistency-type/example

```json
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
```
