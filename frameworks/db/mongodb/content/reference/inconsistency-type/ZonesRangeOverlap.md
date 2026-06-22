---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/ZonesRangeOverlap.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
