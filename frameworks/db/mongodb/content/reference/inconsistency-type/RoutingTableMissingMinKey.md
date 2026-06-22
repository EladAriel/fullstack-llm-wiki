---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/RoutingTableMissingMinKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

########################## RoutingTableMissingMinKey ##########################

# Description

# Format

```json
{
   type: "RoutingTableMissingMinKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      minKeyObj: { <document> },
      globalMin: { <document> }
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
            type: "RoutingTableMissingMinKey",
            description: "Routing table has a gap because first chunk does not start from MinKey",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               minKeyObj: { 
                  x: 0 
               },
               globalMin: { 
                  x: MinKey 
               }
            }
         }
      ],
   },
   ok: 1
}
```
