---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/InconsistentIndex.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

################# InconsistentIndex #################

# Description

# Format

```json
{
   type: "InconsistentIndex",
   description: "<string>",
   details: {
      namespace: "<string>",
      info: <document>
   }
}
```

|incon-type| inconsistency documents contain the following fields:

# Example

Use the :method:`db.adminCommand` method to call the :dbcommand:`checkMetadataConsistency` command:

```javascript
db.adminCommand( { 
   checkMetadataConsistency: 1,
   checkIndexes: true
} )
```

The method returns a cursor with a batch of documents showing the inconsistencies found in the sharding metadata.  The example below shows a cursor with a |incon-type| inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "InconsistentIndex",
            description: "Found an index of a sharded collection that is inconsistent between different shards",
            details: {
               namespace: "test.authors",
               info: {
                   missingFromShards: [
                      "shard-rs1"
                   ],
                   inconsistentProperties: [ ],
                   indexName: "index1"
               }
            }
         }
      ],
   },
   ok: 1
}
```
