---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/revokeRolesFromRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# revokeRolesFromRole (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {  
     revokeRolesFromRole: "<role>",
     roles: [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

.. include:: /includes/fact-roles-array-contents.rst

## Required Access

.. include:: /includes/access-revoke-roles.rst

## Example

The `purchaseAgents` role in the `emea` database inherits privileges from several other roles, as listed in the `roles` array:

```javascript
{
   "_id" : "emea.purchaseAgents",
   "role" : "purchaseAgents",
   "db" : "emea",
   "privileges" : [],
   "roles" : [
      {
         "role" : "readOrdersCollection",
         "db" : "emea"
      },
      {
         "role" : "readAccountsCollection",
         "db" : "emea"
      },
      {
         "role" : "writeOrdersCollection",
         "db" : "emea"
      }
   ]
}
```

The following :dbcommand:`revokeRolesFromRole` operation on the `emea` database removes two roles from the `purchaseAgents` role:

```javascript
use emea
db.runCommand( { revokeRolesFromRole: "purchaseAgents",
                 roles: [
                          "writeOrdersCollection",
                          "readOrdersCollection"
                        ],
                  writeConcern: { w: "majority" , wtimeout: 5000 }
             } )
```

The `purchaseAgents` role now contains just one role:

```javascript
{
   "_id" : "emea.purchaseAgents",
   "role" : "purchaseAgents",
   "db" : "emea",
   "privileges" : [],
   "roles" : [
      {
         "role" : "readAccountsCollection",
         "db" : "emea"
      }
   ]
}
```
