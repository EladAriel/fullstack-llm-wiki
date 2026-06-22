---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/rename.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
