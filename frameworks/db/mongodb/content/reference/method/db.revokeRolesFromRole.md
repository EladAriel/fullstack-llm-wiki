---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.revokeRolesFromRole.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# db.revokeRolesFromRole() (mongosh method)

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

The following :method:`db.revokeRolesFromRole()` operation on the `emea` database removes two roles from the `purchaseAgents` role:

```javascript
use emea
db.revokeRolesFromRole( "purchaseAgents",
                        [
                          "writeOrdersCollection",
                          "readOrdersCollection"
                        ],
                        { w: "majority" , wtimeout: 5000 }
                      )
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
