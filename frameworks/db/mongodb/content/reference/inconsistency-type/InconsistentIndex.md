---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/InconsistentIndex.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
