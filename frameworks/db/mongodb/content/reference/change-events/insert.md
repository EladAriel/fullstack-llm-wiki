---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/insert.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
