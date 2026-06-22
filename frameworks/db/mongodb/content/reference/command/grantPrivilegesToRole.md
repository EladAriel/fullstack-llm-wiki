---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/grantPrivilegesToRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# grantPrivilegesToRole (database command)

## Definition

```javascript
db.runCommand(
   {
     grantPrivilegesToRole: "<role>",
     privileges: [
       {
         resource: { <resource> }, actions: [ "<action>", ... ]
       },
       ...
     ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Command Fields

The command has the following fields:

## Behavior

A role's privileges apply to the database where the role is created. A role created on the `admin` database can include privileges that apply to all databases or to the `cluster <resource-cluster>`.

## Required Access

.. include:: /includes/access-grant-privileges.rst

## Example

The following :dbcommand:`grantPrivilegesToRole` command grants two additional privileges to the `service` role that exists in the `products` database:

```javascript
use products
db.runCommand(
   {
     grantPrivilegesToRole: "service",
     privileges: [
         {
           resource: { db: "products", collection: "" }, actions: [ "find" ]
         },
         {
           resource: { db: "products", collection: "system.js" }, actions: [ "find" ]
         }
     ],
     writeConcern: { w: "majority" , wtimeout: 5000 }
   }
)
```

The first privilege in the `privileges` array allows the user to search on all non-system collections in the `products` database. The privilege does not allow queries on `system collections </reference/system-collections>`, such as the `system.js <<database>.system.js>` collection. To grant access to these system collections, explicitly provision access in the `privileges` array. See `/reference/resource-document`.

The second privilege explicitly allows the :authaction:`find` action on `system.js <<database>.system.js>` collections on all databases.
