---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.updateUser.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# db.updateUser() (mongosh method)

## Definition

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

The :method:`db.updateUser()` method wraps the :dbcommand:`updateUser` command.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

### Encryption

.. include:: /includes/fact-cleartext-passwords-tls.rst

## Required Access

.. include:: /includes/access-update-user.rst

.. include:: /includes/access-change-own-password-and-custom-data.rst

## Example

Given a user `appClient01` in the `products` database with the following user info:

```javascript
{
   _id : "products.appClient01",
   userId : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   user : "appClient01",
   db : "products",
   customData : { empID : "12345", badge : "9156" },
   roles : [
       {
         role : "readWrite",
         db : "products"
       },
       {
         role : "read",
         db : "inventory"
       }
   ],
   mechanisms : [ 
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ],
   authenticationRestrictions : [ {
      clientSource: ["69.89.31.226"],
      serverAddress: ["172.16.254.1"]
   } ]
}
```

The following :method:`db.updateUser()` method **completely** replaces the user's `customData` and `roles` data:

```javascript
use products
db.updateUser( "appClient01",
{
   customData : { employeeId : "0x3039" },
   roles : [
      { role : "read", db : "assets"  }
   ]
} )
```

The user `appClient01` in the `products` database now has the following user information:

```javascript
{
   _id : "products.appClient01",
   userId : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   user : "appClient01",
   db : "products",
   customData : { employeeId : "0x3039" },
   roles : [
       {
         role : "read",
         db : "assets"
       }
   ],
   mechanisms : [
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ],
   authenticationRestrictions : [ {
      clientSource: ["69.89.31.226"],
      serverAddress: ["172.16.254.1"]
   } ]
}
```

### Update User to Use `SCRAM-SHA-256` Credentials Only

> **Note:** To use `SCRAM-SHA-256 <authentication-scram-sha-256>`, the
`featureCompatibilityVersion` must be set to `4.0`. For more
information on featureCompatibilityVersion, see `view-fcv` and
:dbcommand:`setFeatureCompatibilityVersion`.

The following operation updates a user who currently have both `SCRAM-SHA-256` and `SCRAM-SHA-1` credentials to have only `SCRAM-SHA-256` credentials.

> **Note:** - If the password is not specified along with the `mechanisms`,
  you can only update the `mechanisms` to a subset of the current
  SCRAM mechanisms for the user.
- If the password is specified along with the `mechanisms`, you
  can specify any supported SCRAM mechanism or mechanisms.
- For `SCRAM-SHA-256`, the `passwordDigestor` must be the
  default value `"server"`.

```javascript
use reporting
db.updateUser(
   "reportUser256",
   {
     mechanisms: [ "SCRAM-SHA-256" ]
   }
)
```
