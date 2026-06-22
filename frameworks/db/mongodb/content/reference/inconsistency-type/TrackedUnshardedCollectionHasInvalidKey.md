---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/TrackedUnshardedCollectionHasInvalidKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
