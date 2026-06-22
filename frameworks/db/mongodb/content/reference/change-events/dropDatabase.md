---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events/dropDatabase.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
