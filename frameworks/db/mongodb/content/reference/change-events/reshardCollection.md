---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/reshardCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================

# reshardCollection Event

## Summary

## Description

## Example

The following example shows a `reshardCollection` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "reshardCollection",
   "collectionUUID": 0,
   "ns": {"db": "reshard_collection_event", "coll": "coll"},
   "operationDescription": {
     "reshardUUID": 0,
     "shardKey": {"newKey": 1},
     "oldShardKey": {"_id": 1},
     "unique": false,
     "numInitialChunks": Long(1),
     "collation": {"locale": "simple"},
     "zones": [
         {"zone": "zone1", "min": {"newKey": {"$minKey": 1}}, "max": {"newKey": {"$maxKey": 1}}}
     ]
   }
}
```
