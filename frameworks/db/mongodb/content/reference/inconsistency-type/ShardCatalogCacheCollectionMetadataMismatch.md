---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/ShardCatalogCacheCollectionMetadataMismatch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# ShardCatalogCacheCollectionMetadataMismatch

## Description

## Format

```json
{
   type: "ShardCatalogCacheCollectionMetadataMismatch",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: UUID("<uuid>"),
      details: "<array>"
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
            type: "ShardCatalogCacheCollectionMetadataMismatch",
            description: "Shard is missing metadata or routing information for the collection",
            details: {
               namespace: "testdb.testcollection",
               collectionUUID: new UUID("6dc337aa-4c0f-4f98-bc3a-bdfb516fbf51"),
               details: []
            }
         }
      ],
   },
   ok: 1
}
```
