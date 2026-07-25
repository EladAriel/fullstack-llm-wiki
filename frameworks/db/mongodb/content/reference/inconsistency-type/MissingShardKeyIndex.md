---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/MissingShardKeyIndex.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

#################### MissingShardKeyIndex ####################

# Description

# Format

```json
{
   type: "MissingShardKeyIndex",
   description: "<string>",
   details: {
      namespace: "<string>",
      shard: "<string>",
      shardKey: { <document> }
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
```
