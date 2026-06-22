---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getSiblingDB.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# db.getSiblingDB() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Example

You can use :method:`db.getSiblingDB()` as an alternative to the `use <database>` helper. This is particularly useful when writing scripts using :binary:`~bin.mongosh` where the `use` helper is not available.

Consider a MongoDB instance with two databases, `users` and `records`. The `active` collection is a part of the `users` database. The `requests` collection is a part of the `records` database.

### Specify a Database

This operation sets the `db` object to point to the database named `users`, and then returns a :method:`document count <db.collection.countDocuments>` for the `active` collection.

```javascript
db = db.getSiblingDB('users')
db.active.countDocuments()
```

### Use Multiple Databases

You can create multiple `db` objects, that refer to different databases, as in the following sequence of operations:

```javascript
users = db.getSiblingDB('users')
records = db.getSiblingDB('records')

users.active.countDocuments()
users.active.findOne()

records.requests.countDocuments()
records.requests.findOne()
```

This operation creates two `db` objects. Each `db` object refers to a different database, `users` or `records`.

For each database, the query returns:

- a :method:`document count <db.collection.countDocuments>`, and
- an :method:`example document <db.collection.findOne>`
from a collection in that database.
