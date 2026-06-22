---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getURI.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# Mongo.getURI() (mongosh method)

## Definition

## Syntax

The command takes the following form:

```javascript
db.getMongo().getURI()
```

You can use this method to return a URI string for a connection, which you can then use to create a new `Mongo()` instance:

```javascript
new Mongo(db.getMongo().getURI())
```

## Example

To return the current connection string, enter the following:
