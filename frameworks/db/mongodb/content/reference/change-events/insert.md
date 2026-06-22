---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/insert.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============

# insert Event

## Summary

## Description

## Behavior

### Update Operations

.. include:: /includes/fact-modify-change-event

## Example

The following example illustrates an `insert` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "insert",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "documentKey": {
      "userName": "alice123",
      "_id": ObjectId("599af247bb69cd89961c986d")
   },
   "fullDocument": {
      "_id": ObjectId("599af247bb69cd89961c986d"),
      "userName": "alice123",
      "name": "Alice"
   }
}
```

The `documentKey field includes both the id` and the `userName` field. This indicates that the `engineering.users` collection is sharded, with a shard key on `userName and id`.

The `fullDocument` document represents the version of the document at the time of the insert.
