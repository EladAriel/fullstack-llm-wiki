---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/delete.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============

# delete Event

## Synopsis

## Description

## Behavior

#### Document Pre- and Post-Images

.. include:: /includes/change-stream-pre-and-post-images-change-events.rst

.. include:: /includes/change-stream-pre-and-post-images-additional-information.rst

## Example

The following example illustrates a `delete` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "delete",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "documentKey": {
      "_id": ObjectId("599af247bb69cd89961c986d")
   }
}
```

The `fullDocument` document is omitted as the document no longer exists at the time the change stream cursor sends the `delete` event to the client.
