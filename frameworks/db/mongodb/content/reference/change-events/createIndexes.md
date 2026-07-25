---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/createIndexes.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================

# createIndexes Event

## Summary

## Description

## Example

The following example shows a `createIndexes` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "createIndexes",
   "clusterTime": Timestamp({ t: 1651257835, i: 1 }),
   "collectionUUID": UUID("06bced37-7cc8-4267-96aa-a58a422153d8"),
   "wallTime": ISODate("2022-04-29T18:43:55.160Z"),
   "ns": {
      "db": "test",
      "coll": "authors"
   },
   "operationDescription": {
      "indexes": [
         { "v": 2, "key": { "name": 1 }, "name": "name_1" }
      ]
   }
}
```
