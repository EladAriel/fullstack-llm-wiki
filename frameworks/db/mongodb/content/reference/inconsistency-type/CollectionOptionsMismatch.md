---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CollectionOptionsMismatch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
