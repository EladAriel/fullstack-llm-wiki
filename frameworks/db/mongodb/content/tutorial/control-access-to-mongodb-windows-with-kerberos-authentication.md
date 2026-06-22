---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/control-access-to-mongodb-windows-with-kerberos-authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Configure MongoDB with Kerberos Authentication on Windows

## Overview

MongoDB Enterprise supports authentication using a `Kerberos service </core/kerberos>`. Kerberos is an industry standard authentication protocol for large client/server systems. Kerberos allows MongoDB and applications to take advantage of existing authentication infrastructure and processes. MongoDB Enterprise only supports the [MIT implementation](https://kerberos.org/)_ of Kerberos.

## Prerequisites

Setting up and configuring a Kerberos deployment is beyond the scope of this document. This tutorial assumes have configured a `Kerberos service principal <kerberos-service-principal>` for each :binary:`mongod.exe` and :binary:`mongos.exe` instance.

.. include:: /includes/fact-kerberos-FQDN-repica-sets.rst

## Procedures

.. include:: /includes/steps/control-access-to-mongodb-windows-with-kerberos-authentication.rst

## Additional Considerations

### Configure `mongos.exe` for Kerberos

To start :binary:`mongos.exe` with Kerberos support, set the :binary:`mongos.exe` parameter :parameter:`authenticationMechanisms` to `GSSAPI`. You must start :binary:`mongos.exe` as the `service principal account <assign-service-principal-name>`:

```bash
mongos.exe --setParameter authenticationMechanisms=GSSAPI <additional mongos options>
```

.. include:: /includes/extracts/default-bind-ip-security-additional-command-line.rst

For example, the following starts a :binary:`~bin.mongos` instance with Kerberos support:

```bash
mongos.exe --setParameter authenticationMechanisms=GSSAPI --configdb shard0.example.net, shard1.example.net,shard2.example.net --keyFile C:\<path>\mongos.keyfile --bind_ip localhost,<hostname(s)|ip address(es)>
```

Modify or include any additional :binary:`mongos.exe` options as required for your configuration. For example, instead of using :option:`--keyFile <mongos --keyFile>` for internal authentication of sharded cluster members, you can use `X.509 member authentication <x509-internal-authentication>` instead.

### Assign Service Principal Name to MongoDB Windows Service

Use `setspn.exe` to assign the service principal name (SPN) to the account running the :binary:`mongod.exe` and the :binary:`mongos.exe` service:

```bash
setspn.exe -S <service>/<fully qualified domain name> <service account name>
```

### Incorporate Additional Authentication Mechanisms

Kerberos authentication (`GSSAPI <security-auth-kerberos>` (Kerberos)) can work alongside:

- MongoDB's SCRAM authentication mechanism:
- `SCRAM-SHA-1 <authentication-scram>`
- `SCRAM-SHA-256 <authentication-scram>`
- MongoDB's authentication mechanism for LDAP:
- `PLAIN <security-auth-ldap>` (LDAP SASL)
- MongoDB's authentication mechanism for X.509:
- `MONGODB-X509 <security-auth-x509>`)
Specify the mechanisms as follows:

```bash
--setParameter authenticationMechanisms=GSSAPI,SCRAM-SHA-256
```

Only add the other mechanisms if in use. This parameter setting does not affect MongoDB's internal authentication of cluster members.

## Testing and Verification

.. include:: /includes/fact-mongokerberos.rst
