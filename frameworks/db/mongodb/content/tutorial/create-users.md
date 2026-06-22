---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/create-users.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Create a User on Self-Managed Deployments

With access control enabled, users must identify themselves. Grant each user one or more `roles <roles>`. A role grants a user `privileges <privileges>` to perform certain `actions <security-user-actions>` on MongoDB `resources <resource-document>`.

Each application and user of a MongoDB system should map to a distinct user. This principle of access isolation facilitates access revocation and ongoing user maintenance. To ensure a system of `least privilege`, only grant the minimal set of privileges required to a user.

The user information on this page applies to self-managed deployments hosted in all of the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

To learn how to create database users on a MongoDB Atlas deployment, see `mongodb-users`.

## Prerequisites

To be able to create users, you need to:

- `enable access control <enable-access-control>`
- `create a user administrator <create-user-admin>`
For routine user creation, you must possess the following permissions:

.. include:: /includes/access-create-user.rst

## Steps

> **Note:** The following procedures use `authentication-scram`
authentication. For information on other authentication
mechanisms, see `create-users-examples`.

To configure database users for your self-managed MongoDB Enterprise or MongoDB Community deployment, follow these steps:

.. include:: /includes/steps/authorization-create-users.rst

> **Seealso:** `/tutorial/manage-users-and-roles`

## Additional Examples

### Username/Password Authentication

The following operation creates a user in the `reporting` database with the specified name, password, and roles.

> **Tip:** .. include:: /includes/extracts/mongosh-password-prompt.rst

```javascript
use reporting
db.createUser(
  {
    user: "reportsUser",
    pwd: passwordPrompt(),  // or cleartext password
    roles: [
       { role: "read", db: "reporting" },
       { role: "read", db: "products" },
       { role: "read", db: "sales" },
       { role: "readWrite", db: "accounts" }
    ]
  }
)
```

### Kerberos Authentication

.. include:: /includes/extracts/create-user-intro-kerberos.rst

For Kerberos authentication, you must add the Kerberos principal as the username. You do not need to specify a password.

The following operation adds the Kerberos principal `reportingapp@EXAMPLE.NET` with read-only access to the `records` database:

```javascript
use $external
db.createUser(
    {
      user: "reportingapp@EXAMPLE.NET",
      roles: [
         { role: "read", db: "records" }
      ]
    }
)
```

> **Seealso:** For more information about setting up Kerberos authentication for
your MongoDB deployment, see the following tutorials:
- `/tutorial/control-access-to-mongodb-with-kerberos-authentication`
- `/tutorial/control-access-to-mongodb-windows-with-kerberos-authentication`

### LDAP Authentication

.. include:: /includes/LDAP-deprecated.rst

.. include:: /includes/extracts/create-user-intro-ldap.rst

For LDAP authentication, you must specify a username. You do not need to specify the password, as that is handled by the LDAP service.

The following operation adds the `reporting` user with read-only access to the `records` database:

```javascript
use $external
db.createUser(
    {
      user: "reporting",
      roles: [
         { role: "read", db: "records" }
      ]
    }
)
```

> **Seealso:** For more information about setting up LDAP authentication for
your MongoDB deployment, see the following tutorials:
- `/tutorial/configure-ldap-sasl-activedirectory`
- `/tutorial/configure-ldap-sasl-openldap`

### X.509 Client Certificate Authentication

.. include:: /includes/extracts/create-user-intro-x509.rst

For X.509 Client Certificate authentication, you must add the value of the `subject` from the client certificate as a MongoDB user. Each unique X.509 client certificate corresponds to a single MongoDB user. You do not need to specify a password.

The following operation adds the client certificate subject `CN=myName,OU=myOrgUnit,O=myOrg,L=myLocality,ST=myState,C=myCountry` user with read-only access to the `records` database.

```javascript
use $external
db.createUser(
    {
      user: "CN=myName,OU=myOrgUnit,O=myOrg,L=myLocality,ST=myState,C=myCountry",
      roles: [
         { role: "read", db: "records" }
      ]
    }
)
```

> **Seealso:** For more information about setting up X.509 Client Certificate
authentication for your MongoDB deployment, see the following
tutorials:
- `/tutorial/configure-x509-client-authentication`

## Next Steps

To manage users, assign roles, and create custom roles for your self-managed MongoDB Enterprise or MongoDB Community deployment, see `/tutorial/manage-users-and-roles`.
