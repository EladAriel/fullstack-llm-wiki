---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/dropDatabase.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================

# dropDatabase Event

## Synopsis

## Description

## Example

The following example illustrates a `dropDatabase` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "dropDatabase",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering"
   }
}
```

A :dbcommand:`dropDatabase` command generates a `drop event <change-streams-drop-event>` for each collection in the database before generating a `dropDatabase` event for the database.

A `dropDatabase` event leads to an `invalidate` event for change streams opened against its own `ns.db` database.
