---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/TrackedUnshardedCollectionHasInvalidKey.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# TrackedUnshardedCollectionHasInvalidKey

## Description

## Format

```json
{
   type: "TrackedUnshardedCollectionHasInvalidKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      uuid: UUID("<uuid>"),
      shardKey: <document>
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
            type: "TrackedUnshardedCollectionHasInvalidKey",
            description: "Found tracked unsharded collection with invalid shard-key",
            details: {
               namespace: "test.authors",
               uuid: UUID("ebfba414-b576-4f77-bb0e-0d56f3a53c55"),
               shardKey: { "name": 1 }
            }
         }
      ],
   },
   ok: 1
}
```
