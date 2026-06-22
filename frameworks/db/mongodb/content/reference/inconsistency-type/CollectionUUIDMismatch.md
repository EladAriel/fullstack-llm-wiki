---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/CollectionUUIDMismatch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

###################### CollectionUUIDMismatch ######################

# Description

# Format

```json
{
   type: "CollectionUUIDMismatch",
   description: "<string>",
   details: {
      namespace: "<string>",
      shard: "<string>",
      localUUID: UUID("<uuid>"),
      uuid: UUID("<uuid>")
   }
}
```

|incon-type| inconsistency documents contain the following fields:

# Example

.. include:: /includes/inconsistency-type/example

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "CollectionUUIIDMismatch",
            description: "Found collection on non primary shard with mismatching UUID",
            details: {
               namespace: "test.authors",
               shard: "shard02",
               localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
               uuid: new UUID("a3153e8a-3544-43ec-928f-37f72b48dee9")
            }
         }
      ],
   },
   ok: 1
}
```
