---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/updateUser.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# updateUser (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command uses the following syntax:

```javascript
db.runCommand(
   { 
     updateUser: "<username>",
     pwd: passwordPrompt(),      // Or  "<cleartext password>"
     customData: { <any information> },
     roles: [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     authenticationRestrictions: [
        {
          clientSource: ["<IP>" | "<CIDR range>", ...],
          serverAddress: ["<IP>", | "<CIDR range>", ...]
        },
        ...
     ],
     mechanisms: [ "<scram-mechanism>", ... ],
     digestPassword: <boolean>,
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

## Behavior

.. include:: /includes/fact-cleartext-passwords-tls.rst

## Required Access

.. include:: /includes/access-update-user.rst

.. include:: /includes/access-change-own-password-and-custom-data.rst

## Example

Given a user `appClient01` in the `products` database with the following user info:

```javascript
{
   "_id" : "products.appClient01",
   "userId" : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   "user" : "appClient01",
   "db" : "products",
   "customData" : { "empID" : "12345", "badge" : "9156" },
   "roles" : [
       { "role" : "readWrite",
         "db" : "products"
       },
       { "role" : "read",
         "db" : "inventory"
       }
   ],
   "mechanisms" : [
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ]
}
```

The following :dbcommand:`updateUser` command **completely** replaces the user's `customData` and `roles` data:

```javascript
use products
db.runCommand( {
   updateUser : "appClient01",
   customData : { employeeId : "0x3039" },
   roles : [ { role : "read", db : "assets" } ]
} )
```

The user `appClient01` in the `products` database now has the following user information:

```javascript
{
   "_id" : "products.appClient01",
   "userId" : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   "user" : "appClient01",
   "db" : "products",
   "customData" : { "employeeId" : "0x3039" },
   "roles" : [
       { "role" : "read",
         "db" : "assets"
       }
   ],
   "mechanisms" : [
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ]

}
```
