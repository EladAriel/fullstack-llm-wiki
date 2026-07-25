---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/modify.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================

# `modify` Event

## Summary

## Description

## Example

The following example shows a `modify` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "modify",
   "clusterTime": Timestamp({ t: 1654878543, i: 1 }),
   "collectionUUID": UUID("47d6baac-eeaa-488b-98ae-893f3abaaf25"),
   "wallTime": ISODate("2022-06-10T16:29:03.704Z"),
   "ns": {
      "db": "test",
      "coll": "authors" },
   "operationDescription": {
      "index": {
         "name": "age_1",
         "hidden": true
      }
   },
   "stateBeforeChange": {
      "collectionOptions": { 
          "uuid": UUID("47d6baac-eeaa-488b-98ae-893f3abaaf25") 
      },
      "indexOptions": {
         "hidden": false
      }
   }
}
```
