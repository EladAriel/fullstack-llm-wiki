---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/invalidate.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================

# invalidate Event

## Summary

## Description

## Example

The following example illustrates an `invalidate` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "invalidate",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>
}
```

Change streams opened on collections raise an `invalidate` event when a `drop <change-event-drop>`, `rename <change-event-rename>`, or `dropDatabase <change-event-dropDatabase>` operation occurs that affects the watched collection.

Change streams opened on databases raise an `invalidate` event when a `dropDatabase <change-event-dropDatabase>` event occurs that affects the watched database.

`invalidate` events close the change stream cursor.

.. include:: /includes/extracts/changestream-invalid-events.rst
