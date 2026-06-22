---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.updateRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# db.updateRole() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

### Scope

.. include:: /includes/fact-roles-privileges-scope.rst

### Privileges

.. include:: /includes/fact-roles-privileges-multiple-collections.rst

## Required Access

.. include:: /includes/access-update-role.rst

## Example

The following :method:`db.updateRole()` method replaces the `admin.system.roles.privileges` and the `admin.system.roles.roles` for the `inventoryControl` role that exists in the `products` database. The method runs on the database that contains `inventoryControl`:

```javascript
use products
db.updateRole(
    "inventoryControl",
    {
      privileges:
          [
            {
              resource: { db:"products", collection:"clothing" },
              actions: [ "update", "createCollection", "createIndex"]
            }
          ],
      roles:
          [
            {
              role: "read",
              db: "products"
            }
          ]
    },
    { w:"majority" }
)
```

To view a role's privileges, use the :dbcommand:`rolesInfo` command.
