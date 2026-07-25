---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/replace.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================

# `replace` Event

## Summary

## Description

## Behavior

#### Document Pre- and Post-Images

.. include:: /includes/change-stream-pre-and-post-images-change-events.rst

.. include:: /includes/change-stream-pre-and-post-images-additional-information.rst

### Update Operations

.. include:: /includes/fact-modify-change-event

## Examples

The following example illustrates a `replace` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "replace",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "documentKey": {
      "_id": ObjectId("599af247bb69cd89961c986d")
   },
   "fullDocument": {
      "_id": ObjectId("599af247bb69cd89961c986d"),
      "userName": "alice123",
      "name": "Alice"
   }
}
```

A `replace` event can result from `replaceOne()` or from an `update` command that performs a full-document replacement.

The `fullDocument` of a `replace` event represents the replacement document after the operation completes.
