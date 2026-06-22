---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CorruptedZoneShardKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

###################### CorruptedZoneShardKey ######################

# Description

# Format

```json
{
   type: "CorruptedZoneShardKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: UUID("<uuid>"),
      zone: <zone>,
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
            type: "CorruptedZoneShardKey",
            description: "Found zone with a shard key pattern violation",
            details: { 
               namespace: "test.authors",
               collection: { 
                  collectionUUID : new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
                  zone : { 
                     ns : "test.authors",
                     tag: "64ddd81656be208c6685da21", 
                     min: { 
                        y: 0 
                     }, 
                     max: { 
                        x: MaxKey 
                     } 
                  }, 
                  shardKeyPattern: { 
                     x: 1 
                  }
               }
            }
         }
      ],
   },
   ok: 1
}
```
