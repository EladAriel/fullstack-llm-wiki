---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/grantRolesToUser.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# grantRolesToUser (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The :dbcommand:`grantRolesToUser` command uses the following syntax:

```javascript
db.runCommand(
   {  
     grantRolesToUser: "<user>",
     roles: [ <roles> ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

.. include:: /includes/fact-roles-array-contents.rst

## Required Access

.. include:: /includes/access-grant-roles.rst

## Example

Given a user `accountUser01` in the `products` database with the following roles:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    }
]
```

The following :dbcommand:`grantRolesToUser` operation gives `accountUser01` the :authrole:`read` role on the `stock` database and the :authrole:`readWrite` role on the `products` database.

```javascript
use products
db.runCommand( { grantRolesToUser: "accountUser01",
                 roles: [
                    { role: "read", db: "stock"},
                    "readWrite"
                 ],
                 writeConcern: { w: "majority" , wtimeout: 2000 }
             } )
```

The user `accountUser01` in the `products` database now has the following roles:

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
