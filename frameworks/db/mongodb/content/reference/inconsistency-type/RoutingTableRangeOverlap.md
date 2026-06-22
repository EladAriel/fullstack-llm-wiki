---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/RoutingTableRangeOverlap.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

########################## RoutingTableRangeOverlap ##########################

# Description

# Format

```json
{
   type: "RoutingTableRangeOverlap",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      chunkA: {<document>},
      chunkB: {<document>}
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
            type: "RoutingTableRangeOverlap",
            description: "Found two overlapping consecutive chunks",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               chunkA: { 
                  _id: ObjectId("64dde749ac6045c92ef3b9ad"), 
                  uuid: new UUID("8c83ea89-ab6b-4ae4-91ab-813cf781284d"), 
                  min: { 
                     x: MinKey 
                  }, 
                  max: { 
                     x: 0 
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
               chunkB: { 
                  _id: ObjectId("64dde749ac6045c92ef3b9af"), 
                  uuid: new UUID("8c83ea89-ab6b-4ae4-91ab-813cf781284d"), 
                  min: { 
                     x: -10 
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
               }
            }
         }
      ],
   },
   ok: 1
}
```
