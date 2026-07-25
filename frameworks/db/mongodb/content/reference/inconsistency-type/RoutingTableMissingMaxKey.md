---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/RoutingTableMissingMaxKey.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
