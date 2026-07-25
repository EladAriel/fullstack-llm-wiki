---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Session.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
