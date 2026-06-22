---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/dropIndexes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# dropIndexes Event

## Synopsis

## Descriptions

## Example

The following example shows a `dropIndexes` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "dropIndexes",
   "clusterTime": <Timestamp>
   "collectionUUID": <uuid>,
   "wallTime": <isodate>,
   "ns": {
      "db": "test",
      "coll": "authors" },
   "operationDescription": {
      "indexes": [
         { "v": 2, "key": { "name": 1 }, "name": "name_1" }
      ]
   }
}
```
