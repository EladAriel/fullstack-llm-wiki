---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CollectionAuxiliaryMetadataMismatch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# CollectionAuxiliaryMetadataMismatch

## Description

## Format

```json
{
   type: "CollectionAuxiliaryMetadataMismatch",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionMetadata: <array>
   }  
}
```

|incon-type| inconsistency documents contain these fields:

## Example

.. include:: /includes/inconsistency-type/example.rst

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "CollectionAuxiliaryMetadataMismatch",
            description: "Found collection with mismatching auxiliary metadata across shards and/or config server",
            details: {
               namespace: "test.authors",
               collectionMetadata: [ 
                  { "md": { "exampleField": 123 }, "shards": [ "shard0" ] },
                  { "md": { "exampleField": 321 }, "shards": [ "shard1" ] }
               ]
            }
         }
      ],
   },
   ok: 1
}
```
