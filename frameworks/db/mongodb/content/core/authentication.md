---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# Authentication on Self-Managed Deployments

.. include:: /includes/LDAP-deprecated.rst

Authentication is the process of verifying the identity of a client. When access control (`authorization <authorization>`) is enabled, MongoDB requires all clients to authenticate themselves to determine their access.

Authentication and `authorization <authorization>` are distinct:

- **Authentication** verifies the identity of a `user <users>`.
- **Authorization** determines the verified user's access to resources
and operations.

## Getting Started

To get started using access control, follow these tutorials:

- `enable-access-control`
- `create-users`
- `authentication-auth-as-user`
## Authentication Mechanisms

.. include:: /includes/fact-authentication-compat-table.rst

### SCRAM Authentication

`Salted Challenge Response Authentication Mechanism (SCRAM) </core/security-scram>` is the default authentication mechanism for MongoDB.

For more information on SCRAM and MongoDB, see:

- `SCRAM Authentication <authentication-scram>`
- `scram-client-authentication`
### X.509 Certificate Authentication

MongoDB supports `X.509 certificate authentication </core/security-x.509>` for client authentication and internal authentication of the members of replica sets and sharded clusters. X.509 certificate authentication requires a secure `TLS/SSL connection </tutorial/configure-ssl>`.

To use MongoDB with X.509, you must use valid certificates generated and signed by a certificate authority. The client X.509 certificates must meet the `client certificate requirements <client-x509-certificates-requirements>`.

For more information on X.509 and MongoDB, see:

- `X.509 Certificate Authentication <security-auth-x509>`
- `x509-client-authentication`
### Kerberos Authentication

[MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced) supports `Kerberos Authentication <security-kerberos>`. Kerberos is an industry standard authentication protocol for large client/server systems that provides authentication using short-lived tokens that are called tickets.

To use MongoDB with Kerberos, you must have a properly configured Kerberos deployment, configured `Kerberos service principals <kerberos-service-principal>` for MongoDB, and a `Kerberos user principal <kerberos-user-principal>` added to MongoDB.

For more information on Kerberos and MongoDB, see:

- `Kerberos Authentication <security-kerberos>`
- `/tutorial/control-access-to-mongodb-with-kerberos-authentication`
- `/tutorial/control-access-to-mongodb-windows-with-kerberos-authentication`
### LDAP Proxy Authentication

[MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced) and [MongoDB Atlas](https://www.mongodb.com/atlas/database)_ support `LDAP Proxy Authentication <security-ldap>` proxy authentication through a Lightweight Directory Access Protocol (LDAP) service.

For more information on LDAP and MongoDB, see:

- `LDAP Proxy Authentication <security-ldap>`
- `/tutorial/configure-ldap-sasl-activedirectory`
- `/tutorial/configure-ldap-sasl-openldap`
- `/tutorial/authenticate-nativeldap-activedirectory`
These mechanisms allow MongoDB to integrate into your existing authentication system.

### OpenID Connect Authentication

.. include:: /includes/fact-oidc-authentication.rst

For more information on OpenID Connect and MongoDB, see:

- `OpenID Connect Authentication <authentication-oidc>`
- `Configure MongoDB with OpenID Connect <configure-oidc>`
- [OpenID Connect](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol)
## Internal / Membership Authentication

In addition to verifying the identity of a client, MongoDB can require members of replica sets and sharded clusters to `authenticate their membership <inter-process-auth>` to their respective replica set or sharded cluster.

## Contents

- Kerberos </core/kerberos>
- LDAP Proxy </core/security-ldap>
- OIDC/OAuth 2.0 </core/oidc/security-oidc>
- Internal </core/security-internal-authentication>
- Localhost Exception </core/localhost-exception>
- Users </core/security-users>
