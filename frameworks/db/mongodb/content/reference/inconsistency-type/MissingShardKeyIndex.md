---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/MissingShardKeyIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
