---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.revokePrivilegesFromRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# db.revokePrivilegesFromRole() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

### Scope

To revoke a privilege, the `resource document </reference/resource-document>` pattern must match **exactly** the `resource` field of that privilege. The `actions` field can be a subset or match exactly.

For example, given the role `accountRole` in the `products` database with the following privilege that specifies the `products` database as the resource:

```javascript
{
  "resource" : {
      "db" : "products",
      "collection" : ""
  },
  "actions" : [
      "find",
      "update"
  ]
}
```

You cannot revoke `find` and/or `update` from just one collection in the `products` database. The following operations result in no change to the role:

```javascript
use products
db.revokePrivilegesFromRole(
   "accountRole",
   [
     {
       resource : {
          db : "products",
          collection : "gadgets"
       },
       actions : [
          "find",
          "update"
       ]
     }
   ]
)

db.revokePrivilegesFromRole(
   "accountRole",
   [
     {
       resource : {
          db : "products",
          collection : "gadgets"
       },
       actions : [
          "find"
       ]
     }
   ]
)
```

To revoke the `"find"` and/or the `"update"` action from the role `accountRole`, you must match the resource document exactly. For example, the following operation revokes just the `"find"` action from the existing privilege.

```javascript
use products
db.revokePrivilegesFromRole(
   "accountRole",
   [
     {
       resource : {
          db : "products",
          collection : ""
       },
       actions : [
          "find"
       ]
     }
   ]
)
```

### Privileges

.. include:: /includes/fact-roles-privileges-multiple-collections.rst

## Required Access

.. include:: /includes/access-revoke-privileges.rst

## Example

The following operation removes multiple privileges from the `associates` role:

```javascript
db.revokePrivilegesFromRole(
   "associate",
   [
     {
       resource: { db: "products", collection: "" },
       actions: [ "createCollection", "createIndex", "find" ]
     },
     {
       resource: { db: "products", collection: "orders" },
       actions: [ "insert" ]
     }
   ],
   { w: "majority" }
)
```
