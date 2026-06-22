---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.grantRolesToRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# db.grantRolesToRole() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

### Scope

A role can inherit privileges from other roles in its database. A role created on the `admin` database can inherit privileges from roles in any database.

## Required Access

.. include:: /includes/access-grant-roles.rst

## Example

The following :method:`db.grantRolesToRole()` operation updates the `productsReaderWriter` role in the `products` database to `inherit <inheritance>` the `privileges <privileges>` of `productsReader` role:

```javascript
use products
db.grantRolesToRole(
    "productsReaderWriter",
    [ "productsReader" ],
    { w: "majority" , wtimeout: 5000 }
)
```
