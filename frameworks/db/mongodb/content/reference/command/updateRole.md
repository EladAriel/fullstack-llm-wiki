---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/updateRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# updateRole (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

To update a role, you must provide the `privileges` array, `roles` array, or both.

The command uses the following syntax:

```javascript
db.runCommand(
   {
     updateRole: "<role>",
     privileges:
         [
           { resource: { <resource> }, actions: [ "<action>", ... ] },
           ...
         ],
     roles:
         [
           { role: "<role>", db: "<database>" } | "<role>",
           ...
         ],
     authenticationRestrictions:
         [
           {
             clientSource: ["<IP>" | "<CIDR range>", ...],
             serverAddress: ["<IP>", ...]
           },
           ...
         ]
     writeConcern: <write concern document>,
     comment: <any>
   }
 )
```

## Command Fields

The command takes the following fields:

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

## Behavior

A role's privileges apply to the database where the role is created. The role can inherit privileges from other roles in its database. A role created on the `admin` database can include privileges that apply to all databases or to the `cluster <resource-cluster>` and can inherit privileges from roles in other databases.

## Required Access

.. include:: /includes/access-update-role.rst

## Example

The following is an example of the :dbcommand:`updateRole` command that updates the `myClusterwideAdmin` role on the `admin` database. While the `admin.system.roles.privileges` and the `admin.system.roles.roles` arrays are both optional, at least one of the two is required:

```javascript
db.adminCommand(
   {
     updateRole: "myClusterwideAdmin",
     privileges:
         [
           {
             resource: { db: "", collection: "" },
             actions: [ "find" , "update", "insert", "remove" ]
           }
         ],
     roles:
         [
           { role: "dbAdminAnyDatabase", db: "admin" }
         ],
     writeConcern: { w: "majority" }
   }
)
```

To view a role's privileges, use the :dbcommand:`rolesInfo` command.
