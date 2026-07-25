---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/ZonesRangeOverlap.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

################# ZonesRangeOverlap #################

# Description

# Format

```json
{
   type: "ZonesRangeOverlap",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      zoneA: {<document>},
      zoneB: {<document>}
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
            type: "ZonesRangeOverlap",
            description: "Found two overlapping zones",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               zoneA: { 
                  ns: "test.authors", 
                  tag: "64ddec77e0d32b766bb8d5fe", 
                  min: { x: MinKey }, 
                  max: { x: 0 } 
               },
               zoneB: { 
                  ns: "test.authors", 
                  tag: "64ddec77e0d32b766bb8d5ff", 
                  min: { x: -10 }, 
                  max: { x: MaxKey }
               }
             }
          }
      ],
   },
   ok: 1
}
```
