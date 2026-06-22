---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/RoutingTableMissingMaxKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

########################## RoutingTableMissingMaxKey ##########################

# Description

# Format

```json
{
   type: "RoutingTableMissingMaxKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      maxKeyObj: { <document> },
      globalMax: { <document> }
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
            type: "RoutingTableMissingMaxKey",
            description: "Routing table has a gap because last chunk boundary does not reach MaxKey",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               maxKeyObj: { 
                  x: 0 
               },
               globalMax: { 
                  x: MaxKey 
               }
            }
         }
      ],
   },
   ok: 1
}
```
