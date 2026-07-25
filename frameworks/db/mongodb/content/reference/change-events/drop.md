---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/drop.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========

# drop Event

## Synopsis

## Description

## Example

The following example illustrates a `drop` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "drop",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   }
}
```

A `drop` event leads to an `invalidate` event for change streams opened against its own `ns` collection.
