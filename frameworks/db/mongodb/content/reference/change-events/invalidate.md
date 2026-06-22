---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/invalidate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
