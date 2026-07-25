---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/ShardCatalogCacheCollectionMetadataMismatch.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
