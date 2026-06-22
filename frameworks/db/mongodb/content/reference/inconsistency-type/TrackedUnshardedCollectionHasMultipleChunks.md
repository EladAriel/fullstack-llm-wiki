---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/TrackedUnshardedCollectionHasMultipleChunks.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# TrackedUnshardedCollectionHasMultipleChunks

## Description

## Format

```json
{
   type: "TrackedUnshardedCollectionHasMultipleChunks",
   description: "<string>",
   details: {
      namespace: "<string>",
      uuid: UUID("<uuid>"),
      numChunks: <integer>
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
            type: "TrackedUnshardedCollectionHasMultipleChunks",
            description: "Found tracked unsharded collection with more than one chunks",
            details: {
               namespace: "test.authors",
               uuid: UUID("0a5ed8eb-d769-456a-8c8b-c67ee99cfd8a"),
               numChunks: 2
            }
         }
      ],
   },
   ok: 1
}
```
