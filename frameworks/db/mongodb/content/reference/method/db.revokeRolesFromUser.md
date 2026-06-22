---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.revokeRolesFromUser.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# db.revokeRolesFromUser() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

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

The following :method:`db.revokeRolesFromUser()` method removes the two of the user's roles: the :authrole:`read` role on the `stock` database and the :authrole:`readWrite` role on the `products` database, which is also the database on which the method runs:

```javascript
use products
db.revokeRolesFromUser( "accountUser01",
                        [ { role: "read", db: "stock" }, "readWrite" ],
                        { w: "majority" }
                      )
```

The user `accountUser01` user in the `products` database now has only one remaining role:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    }
]
```
