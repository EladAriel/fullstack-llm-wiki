---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.createRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# db.createRole() (mongosh method)

## Definition

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

### Scope

.. include:: /includes/fact-roles-privileges-scope.rst

The :method:`db.createRole()` method returns a duplicate role error if the role already exists in the database.

### Privileges

.. include:: /includes/fact-roles-privileges-multiple-collections.rst

## Required Access

.. include:: /includes/access-create-role.rst

## Example

The following :method:`db.createRole()` method creates the `myClusterwideAdmin` role on the `admin` database:

```javascript
use admin
db.createRole(
   {
     role: "myClusterwideAdmin",
     privileges: [
       { resource: { cluster: true }, actions: [ "addShard" ] },
       { resource: { db: "config", collection: "" }, actions: [ "find", "update", "insert", "remove" ] },
       { resource: { db: "users", collection: "usersCollection" }, actions: [ "update", "insert", "remove" ] },
       { resource: { db: "", collection: "" }, actions: [ "find" ] }
     ],
     roles: [
       { role: "read", db: "admin" }
     ]
   },
   { w: "majority" , wtimeout: 5000 }
)
```
