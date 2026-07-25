---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/MissingLocalCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================

# MissingLocalCollection

## Description

## Format

```json
{
   type: "MissingLocalCollection",
   description: "<string>",
   details: {
      namespace: "<string>",
      uuid: UUID("<uuid>"),
      shard: "<string>"
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
            type: "MissingLocalCollection",
            description: "Collection registered on the sharding catalog not found on the given shards",
            details: {
               namespace: "test.authors",
               uuid: UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
               shard: "shard02"
            }
         }
      ],
   },
   ok: 1
}
```
