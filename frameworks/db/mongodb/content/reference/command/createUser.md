---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/createUser.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# createUser (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
db.runCommand(
   {
     createUser: "<name>",
     pwd: passwordPrompt(),      // Or  "<cleartext password>"
     customData: { <any information> },
     roles: [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     writeConcern: { <write concern> },
     authenticationRestrictions: [
        { clientSource: [ "<IP|CIDR range>", ... ], serverAddress: [ "<IP|CIDR range>", ... ] }, 
        ...
     ],
     mechanisms: [ "<scram-mechanism>", ... ], 
     digestPassword: <boolean>,
     comment: <any>
   }
)
```

### Command Fields

:dbcommand:`createUser` has the following fields:

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

## Behavior

### User ID

MongoDB automatically assigns a unique `userId` to the user upon creation.

### Encryption

.. include:: /includes/fact-cleartext-passwords-tls.rst

### External Credentials

Users created on the `$external` database should have credentials stored externally to MongoDB, as, for example, with `MongoDB Enterprise installations that use Kerberos </tutorial/control-access-to-mongodb-with-kerberos-authentication>`.

.. include:: /includes/extracts/sessions-external-username-limit.rst

### `local` Database

You cannot create users on the local database.

### Username Limits

Usernames must consist of at least one character and cannot be larger than 7MB.

## Required Access

.. include:: /includes/access-create-user.rst

## Example

The following :dbcommand:`createUser` command creates a user `accountAdmin01` on the `products` database. The command gives `accountAdmin01` the `clusterAdmin` and `readAnyDatabase` roles on the `admin` database and the `readWrite` role on the `products` database:

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
db.getSiblingDB("products").runCommand( {
      createUser: "accountAdmin01",
      pwd: passwordPrompt(), 
      customData: { employeeId: 12345 },
      roles: [
               { role: "clusterAdmin", db: "admin" },
               { role: "readAnyDatabase", db: "admin" },
               "readWrite"
             ],
      writeConcern: { w: "majority" , wtimeout: 5000 }
} )
```
