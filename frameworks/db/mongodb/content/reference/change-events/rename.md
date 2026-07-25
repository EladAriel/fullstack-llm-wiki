---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/rename.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================

# `rename` Event

## Summary

## Description

## Behavior

#### Expanded Event Information

.. versionchanged:: 6.0

Starting in MongoDB 6.0, when the `showExpandedEvents <change-streams-expanded-events>` option is set to `true` for the change stream, the `rename` event includes an `operationDescription` document. This document provides a `to` field showing the changed database and collection and a `dropTarget` field indicating whether the `rename` operation removed the collection before the rename.

## Example

The following example illustrates a `rename` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "rename",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "to": {
      "db": "engineering",
      "coll": "people"
   },
   "operationDescription": {
      "to": {
         "db": "engineering",
         "coll": "people"
      }
   }
}
```

A `rename` event leads to an `invalidate event <change-event-invalidate>` for change streams opened against its `ns` collection or `to` collection.
