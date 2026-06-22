---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/createRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# createRole (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     createRole: "<new role>",
     privileges: [
       { resource: { <resource> }, actions: [ "<action>", ... ] },
       ...
     ],
     roles: [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     authenticationRestrictions: [
       {
         clientSource: ["<IP>" | "<CIDR range>", ...],
         serverAddress: ["<IP>" | "<CIDR range>", ...]
       },
       ...
     ],
     writeConcern: <write concern document>,
     comment: <any>
   }
)
```

### Command Fields

The :dbcommand:`createRole` command has the following fields:

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

## Behavior

A role's privileges apply to the database where the role is created. The role can inherit privileges from other roles in its database. A role created on the `admin` database can include privileges that apply to all databases or to the `cluster <resource-cluster>` and can inherit privileges from roles in other databases.

## Required Access

.. include:: /includes/access-create-role.rst

## Example

The following :dbcommand:`createRole` command creates the `myClusterwideAdmin` role on the `admin` database:

```javascript
db.adminCommand({ createRole: "myClusterwideAdmin",
  privileges: [
    { resource: { cluster: true }, actions: [ "addShard" ] },
    { resource: { db: "config", collection: "" }, actions: [ "find", "update", "insert", "remove" ] },
    { resource: { db: "users", collection: "usersCollection" }, actions: [ "update", "insert", "remove" ] },
    { resource: { db: "", collection: "" }, actions: [ "find" ] }
  ],
  roles: [
    { role: "read", db: "admin" }
  ],
  writeConcern: { w: "majority" , wtimeout: 5000 }
})
```
