---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.grantPrivilegesToRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# db.grantPrivilegesToRole() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

### Scope

Except for roles created in the `admin` database, a role can only include privileges that apply to its database

A role created in the `admin` database can include privileges that apply to the `admin` database, other databases or to the `cluster <resource-cluster>` resource.

### Privileges

.. include:: /includes/fact-roles-privileges-multiple-collections.rst

## Required Access

.. include:: /includes/access-grant-privileges.rst

## Example

The following :method:`db.grantPrivilegesToRole()` operation grants two additional privileges to the role `inventoryCntrl01`, which exists on the `products` database. The operation is run on that database:

```javascript
use products
db.grantPrivilegesToRole(
  "inventoryCntrl01",
  [
    {
      resource: { db: "products", collection: "" },
      actions: [ "insert" ]
    },
    {
      resource: { db: "products", collection: "system.js" },
      actions: [ "find" ]
    }
  ],
  { w: "majority" }
)
```

The first privilege permits users with this role to perform the `insert` `action <security-user-actions>` on all collections of the `products` database, except the `system collections </reference/system-collections>`. To access a system collection, a privilege must explicitly specify the system collection in the resource document, as in the second privilege.

The second privilege permits users with this role to perform the :authaction:`find` `action <security-user-actions>` on the `product` database's system collection named `system.js <<database>.system.js>`.
