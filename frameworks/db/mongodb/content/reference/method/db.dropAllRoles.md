---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.dropAllRoles.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# db.dropAllRoles() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

## Required Access

.. include:: /includes/access-drop-role.rst

## Example

The following operations drop all `user-defined <user-defined-roles>` roles from the `products` database and uses a `write concern <write-concern-operation>` of `majority`.

```javascript
use products
db.dropAllRoles( { w: "majority" } )
```

The method returns the number of roles dropped:

```javascript
4
```
