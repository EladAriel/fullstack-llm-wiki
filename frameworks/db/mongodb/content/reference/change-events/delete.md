---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/delete.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
