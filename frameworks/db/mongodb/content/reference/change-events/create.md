---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/create.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============

# create Event

## Summary

## Description

## Example

The following example shows a `create` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "create",
   "clusterTime": Timestamp({ t: 1654894547, i: 24 }),
   "collectionUUID": UUID("98046a1a-b649-4e5b-9c75-67594221ce19"),
   "wallTime": ISODate("2022-06-10T20:55:47.947Z"),
   "ns": {
      "db": "test",
      "coll": "names"
   },
   "operationDescription": {
      "idIndex": { "v": 2, "key": { _id: 1 }, "name": "_id_" }
   }
}
```
