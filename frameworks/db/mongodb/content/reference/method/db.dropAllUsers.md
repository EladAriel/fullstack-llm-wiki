---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.dropAllUsers.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# db.dropAllUsers() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

## Required Access

.. include:: /includes/access-drop-user.rst

## Example

The following :method:`db.dropAllUsers()` operation drops every user from the `products` database.

```javascript
use products
db.dropAllUsers( {w: "majority", wtimeout: 5000} )
```

The `n` field in the results document shows the number of users removed:

```javascript
{ "n" : 12, "ok" : 1 }
```
