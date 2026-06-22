---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Session.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======

# Session

## Definition

## Example

The following example starts a session on the :method:`Mongo` connection object associated with :binary:`~bin.mongosh`'s global `db` variable, and then uses the :method:`Session.getDatabase()` method to retrieve the database object associated with the session.

```javascript
var session = db.getMongo().startSession();
db = session.getDatabase(db.getName());
```

## Contents

- /reference/method/Session.abortTransaction
- /reference/method/Session.commitTransaction
- /reference/method/Session.startTransaction
- /reference/method/Session.withTransaction
