---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getURI.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
