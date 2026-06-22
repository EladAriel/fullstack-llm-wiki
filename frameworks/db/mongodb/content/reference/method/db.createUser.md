---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.createUser.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# db.createUser() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

### Roles

.. include:: /includes/fact-roles-array-contents.rst

### Authentication Restrictions

.. include:: /includes/fact-auth-restrictions-array-contents.rst

The :method:`db.createUser()` method wraps the :dbcommand:`createUser` command.

## Behavior

### User ID

MongoDB automatically assigns a unique `userId` to the user upon creation.

### Replica set

.. include:: /includes/fact-management-methods-write-concern.rst

### Encryption

.. include:: /includes/fact-cleartext-passwords-tls.rst

### External Credentials

Users created on the `$external` database should have credentials stored externally to MongoDB, as, for example, with `MongoDB Enterprise installations that use Kerberos </tutorial/control-access-to-mongodb-with-kerberos-authentication>`.

.. include:: /includes/extracts/sessions-external-username-limit.rst

### `local` Database

You cannot create users on the local database.

## Required Access

.. include:: /includes/access-create-user.rst

## Examples

The following :method:`db.createUser()` operation creates the `accountAdmin01` user on the `products` database.

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
use products
db.createUser( { user: "accountAdmin01",
                 pwd: passwordPrompt(),  // Or  "<cleartext password>"
                 customData: { employeeId: 12345 },
                 roles: [ { role: "clusterAdmin", db: "admin" },
                          { role: "readAnyDatabase", db: "admin" },
                          "readWrite"] },
               { w: "majority" , wtimeout: 5000 } )
```

The operation gives `accountAdmin01` the following roles:

- the `clusterAdmin` and `readAnyDatabase` roles on the `admin`
database

- the `readWrite` role on the `products` database
### Create User with Roles

The following operation creates `accountUser` in the `products` database and gives the user the `readWrite` and `dbAdmin` roles.

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
use products
db.createUser(
   {
     user: "accountUser",
     pwd: passwordPrompt(),  // Or  "<cleartext password>"
     roles: [ "readWrite", "dbAdmin" ]
   }
)
```

### Create User without Roles

The following operation creates a user named `reportsUser` in the `admin` database but does not yet assign roles:

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
use admin
db.createUser(
   {
     user: "reportsUser",
     pwd: passwordPrompt(),  // Or  "<cleartext password>"
     roles: [ ]
   }
)
```

### Create Administrative User with Roles

The following operation creates a user named `appAdmin` in the `admin` database and gives the user `readWrite` access to the `config` database, which lets the user change certain settings for sharded clusters, such as to the balancer setting.

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
use admin
db.createUser(
   {
     user: "appAdmin",
     pwd: passwordPrompt(),   // Or  "<cleartext password>"
     roles:
       [
         { role: "readWrite", db: "config" },
         "clusterAdmin"
       ]
   }
)
```

### Create User with Authentication Restrictions

The following operation creates a user named `restricted` in the `admin` database. This user may only authenticate if connecting from IP address `192.0.2.0` to IP address `198.51.100.0`.

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
use admin
db.createUser(
   {
     user: "restricted",
     pwd: passwordPrompt(),      // Or  "<cleartext password>"
     roles: [ { role: "readWrite", db: "reporting" } ],
     authenticationRestrictions: [ {
        clientSource: ["192.0.2.0"],
        serverAddress: ["198.51.100.0"]
     } ]
   }
)
```

### Create User with `SCRAM-SHA-256` Credentials Only

> **Note:** To use `SCRAM-SHA-256 <authentication-scram-sha-256>`, the
`featureCompatibilityVersion` must be set to `4.0`. For more
information on featureCompatibilityVersion, see `view-fcv` and
:dbcommand:`setFeatureCompatibilityVersion`.

The following operation creates a user with only `SCRAM-SHA-256` credentials.

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
use reporting
db.createUser(
   {
     user: "reportUser256",
     pwd: passwordPrompt(),   // Or  "<cleartext password>"
     roles: [ { role: "readWrite", db: "reporting" } ],
     mechanisms: [ "SCRAM-SHA-256" ]
   }
)
```

If the :parameter:`authenticationMechanisms` parameter is set, the `mechanisms` field can only include values specified in the :parameter:`authenticationMechanisms` parameter.
