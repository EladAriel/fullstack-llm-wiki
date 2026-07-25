---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/revokeRolesFromUser.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# revokeRolesFromUser (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     revokeRolesFromUser: "<user>",
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

The command takes the following fields:

.. include:: /includes/fact-roles-array-contents.rst

## Required Access

.. include:: /includes/access-revoke-roles.rst

## Example

The `accountUser01` user in the `products` database has the following roles:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    },
    { "role" : "read",
      "db" : "stock"
    },
    { "role" : "readWrite",
      "db" : "products"
    }
]
```

The following :dbcommand:`revokeRolesFromUser` command removes the two of the user's roles: the :authrole:`read` role on the `stock` database and the :authrole:`readWrite` role on the `products` database, which is also the database on which the command runs:

```javascript
use products
db.runCommand( { revokeRolesFromUser: "accountUser01",
                 roles: [
                          { role: "read", db: "stock" },
                          "readWrite"
                 ],
                 writeConcern: { w: "majority" }
             } )
```

The user `accountUser01` in the `products` database now has only one remaining role:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    }
]
```
