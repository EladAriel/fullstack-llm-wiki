---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/reshardCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
