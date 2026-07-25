---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CollectionOptionsMismatch.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================

# CollectionOptionsMismatch

## Description

## Format

```json
{
   type: "CollectionOptionsMismatch",
   description: "<string>",
   details: {
      namespace: "<string>",
      options: <array>
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
            type: "CollectionOptionsMismatch",
            description: "Found collection with mismatching options across shards and/or config server",
            details: {
               namespace: "test.authors",
               options: [ 
                  { "options": { "capped": true }, "shards": [ "shard0" ] },
                  { "options": { "capped": false }, "shards": [ "shard1", "config" ] }
               ]
            }
         }
      ],
   },
   ok: 1
}
```
