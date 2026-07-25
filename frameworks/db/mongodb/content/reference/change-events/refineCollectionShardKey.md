---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/refineCollectionShardKey.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# refineCollectionShardKey Event

## Summary

## Description

## Example

The following example shows a `refineCollectionShardKey` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "refineCollectionShardKey",
   "clusterTime": Timestamp({ t: 1654894852, i: 52 }),
   "collectionUUID": UUID("98046a1a-b649-4e5b-9c75-67594221ce19"),
   "ns": {"db": "reshard_collection_event", "coll": "coll"},
   "operationDescription": {
     "shardKey": {"_id": 1, akey: 1}, 
     "oldShardKey": {"_id": 1}
   }
}
```
