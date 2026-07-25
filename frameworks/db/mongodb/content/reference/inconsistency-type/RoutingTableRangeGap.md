---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/RoutingTableRangeGap.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

########################## RoutingTableRangeGap ##########################

# Description

# Format

```json
{
   type: "RoutingTableRangeGap",
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
            type: "RoutingTableRangeGap",
            description: "Found a gap between two consecutive chunks",
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
                     x: 10
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
