---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/MissingLocalCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
