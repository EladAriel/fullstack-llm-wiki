---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/grantRolesToRole.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================

# grantRolesToRole (database command)

## Definition

The command has the following syntax:

```javascript
db.runCommand(
   {  
     grantRolesToRole: "<role>",
     roles: [
                { role: "<role>", db: "<database>" },
                ...
            ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

The command has the following fields:

.. include:: /includes/fact-roles-array-contents.rst

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

A role can inherit privileges from other roles in its database. A role created on the `admin` database can inherit privileges from roles in any database.

## Required Access

.. include:: /includes/access-grant-roles.rst

## Example

The following :dbcommand:`grantRolesToRole` command updates the `productsReaderWriter` role in the `products` database to `inherit <inheritance>` the `privileges <privileges>` of the `productsReader` role in the `products` database:

```javascript
use products
db.runCommand(
   { grantRolesToRole: "productsReaderWriter",
     roles: [
              "productsReader"
     ],
     writeConcern: { w: "majority" , wtimeout: 5000 }
   }
)
```
