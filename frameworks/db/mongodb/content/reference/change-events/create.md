---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/create.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
