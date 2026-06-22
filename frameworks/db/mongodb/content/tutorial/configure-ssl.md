---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-ssl.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# Configure MongoDB Instances for TLS/SSL Encryption

## Overview

This document helps you to configure a new MongoDB instance to support TLS/SSL. For instructions on upgrading a cluster currently not using TLS/SSL to using TLS/SSL, see `/tutorial/upgrade-cluster-to-ssl` instead.

To set up a local development environment with TLS/SSL, see `develop-mongodb-locally-with-tls`.

.. include:: /includes/fact-tls-libraries.rst

> **Note:** - .. include:: /includes/fact-tls-1.0.rst
- MongoDB's TLS/SSL encryption only allows the use of strong TLS/SSL
  ciphers with a minimum of 128-bit key length for all connections.
- The Linux 64-bit legacy x64 builds of MongoDB do **not** include
  support for TLS/SSL.

## Prerequisites

> **Important:** .. include:: /includes/extracts/security-prereq-configure-ssl.rst

### Certificate Authorities

.. include:: /includes/fact-ssl-certificate-authorities.rst

Member Certificate Requirements ```````````````````````````````

.. include:: /includes/extracts/x509-certificate-member.rst

### `mongod` and `mongos` Certificate Key File

When establishing a TLS/SSL connection, the :binary:`mongod` / :binary:`mongos` presents a certificate key file to its clients to establish its identity. [#FIPS]_ The certificate key file contains a public key certificate and its associated private key, but only the public component is revealed to the client.

MongoDB can use any valid TLS/SSL certificate issued by a certificate authority, or a self-signed certificate. If you use a self-signed certificate, although the communications channel will be encrypted to prevent eavesdropping on the connection, there will be no validation of server identity. This leaves you vulnerable to a man-in-the-middle attack. Using a certificate signed by a trusted certificate authority will permit MongoDB drivers to verify the server's identity.

In general, avoid using self-signed certificates unless the network is trusted.

With regards to certificates for replica set and sharded cluster members, it is advisable to use different certificates on different servers. This minimizes exposure of the private key and allows for hostname validation.

> **Note:** If a MongoDB deployment is not configured to use a CA file, it bypasses client
certificate validation.

For FIPS mode, ensure that the certificate is FIPS-compliant (i.e uses a FIPS-compliant algorithm) and the private key meets the PKCS#8 standard. If you need to convert a private key to PKCS#8 format, various conversion tools exist, such as `openssl pkcs8` and others.

## Procedures (Using `net.tls` Settings)

> **Note:** .. include:: /includes/fact-net-tls-ssl.rst
The procedures in this section use the `net.tls` settings. For
procedures using the `net.ssl` alias, see `configure-ssl`.

### Create a PEM File From Raw Certificate Data

To configure MongoDB with TLS/SSL, you need a single PEM file containing both the private key and the full certificate chain.

If you have raw certificate data, such as a private key `privkey.pem` and a certificate chain file `fullchain.pem`, you can create the required PEM file by concatenating these files:

```sh
cat privkey.pem fullchain.pem > mongodb.pem
```

The resulting `mongodb.pem` file must contain the private key and the certificate chain with their full RFC-7468 encapsulation boundaries, `BEGIN` and `END`.

In your MongoDB configuration, provide the path to the `mongodb.pem` file as the value of the :setting:`net.tls.certificateKeyFile`.

Additionally, point the `net.tls.CAFile` setting to the full chain file `fullchain.pem`, which contains the certificate chain for verifying the client certificate.

### Set Up `mongod` and `mongos` with TLS/SSL Certificate and Key

The following section configures :binary:`mongod` / :binary:`mongos` to use TLS/SSL connections. With these TLS/SSL settings, :binary:`mongod` / :binary:`mongos` presents its certificate key file to the client. However, the :binary:`mongod` / :binary:`mongos` does not require a certificate key file from the client to verify the client's identity. To require client's certificate key file, see `ssl-mongod-ca-signed-ssl-cert-key` instead.

> **Note:** The procedure uses the `net.tls` settings. For procedures that use the
`net.ssl` settings, see `configure-ssl`.

To use TLS/SSL connections, include the following `TLS/SSL settings <net-tls-conf-options>` in your :binary:`mongod` / :binary:`mongos` instance's `configuration file <conf-file>`:

A :binary:`~bin.mongod` instance that uses the above configuration can only accept TLS/SSL connections:

```bash
mongod --config <path/to/configuration/file>
```

See `tls-client-connection-only` for more information on connecting with TLS/SSL.

> **Seealso:** You can also configure :binary:`~bin.mongod` and
:binary:`~bin.mongos` using command-line options instead of the
configuration file:
- For :binary:`~bin.mongod`, see: :option:`--tlsMode <mongod --tlsMode>`;
  :option:`--tlsCertificateKeyFile <mongod --tlsCertificateKeyFile>`; and
  :option:`--tlsCertificateSelector <mongod --tlsCertificateSelector>`.
- For  :binary:`~bin.mongos`, see: :option:`--tlsMode <mongos --tlsMode>`;
  :option:`--tlsCertificateKeyFile <mongos --tlsCertificateKeyFile>`; and
  :option:`--tlsCertificateSelector <mongos --tlsCertificateSelector>`.

### Set Up `mongod` and `mongos` with Client Certificate Validation

The following section configures :binary:`mongod` / :binary:`mongos` to use TLS/SSL connections and perform client certificate validation. With these TLS/SSL settings:

- :binary:`mongod` / :binary:`mongos` presents its certificate
key file to the client for verification.

- :binary:`mongod` / :binary:`mongos` requires a certificate
key file from the client to verify the client's identity.

> **Note:** The procedure uses the `net.tls` settings For procedures that use the
`net.ssl` settings, see `configure-ssl`.

To use TLS/SSL connections and perform client certificate validation, include the following `TLS/SSL settings <net-tls-conf-options>` in your :binary:`mongod` / :binary:`mongos` instance's `configuration file <conf-file>`:

> **Note:** You can use system SSL certificate stores for Windows and macOS. To use the
system SSL certificate store, specify `net.ssl.certificateSelector` instead
of specifying the certificate key file.

> **Important:** .. include:: /includes/fact-ssl-tlsCAFile-tlsUseSystemCA.rst

For example, consider the following `configuration file <conf-file>` for a :binary:`~bin.mongod` instance:

```yaml
net:
   tls:
      mode: requireTLS
      certificateKeyFile: /etc/ssl/mongodb.pem
      CAFile: /etc/ssl/caToValidateClientCertificates.pem
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
storage:
   dbPath: "/var/lib/mongodb"
processManagement:
   fork: true
net:
   bindIp: localhost,mongodb0.example.net
   port: 27017
```

A :binary:`~bin.mongod` instance that uses the above configuration can only accept TLS/SSL connections and requires a valid certificate from its clients:

```bash
mongod --config <path/to/configuration/file>
```

Clients must specify TLS/SSL connections and present their certificate key file to the instance. See `mongo-connect-require-client-certificates-tls` for more information on connecting with TLS/SSL.

> **Seealso:** You can also configure :binary:`~bin.mongod` and
:binary:`~bin.mongos` using command-line options instead of the
configuration file:
- For :binary:`~bin.mongod`, see :option:`--tlsMode <mongod --tlsMode>`,
  :option:`--tlsCertificateKeyFile <mongod --tlsCertificateKeyFile>`, and
  :option:`--tlsCAFile <mongod --tlsCAFile>`.
- For  :binary:`~bin.mongos`, see :option:`--tlsMode <mongos --tlsMode>`,
  :option:`--tlsCertificateKeyFile <mongos --tlsCertificateKeyFile>`,
  :option:`--tlsCAFile <mongos --tlsCAFile>`.

Block Revoked Certificates for Clients ``````````````````````````````````````

> **Note:** The procedure uses the `net.tls` settings. For procedures that use the
`net.ssl` settings, see `configure-ssl`.

.. include:: /includes/security/block-revoked-certificates-intro.rst

To specify a :abbr:`CRL (Certificate Revocation List)` file, include :setting:`net.tls.CRLFile` set to a file that contains revoked certificates.

For example:

```yaml
net:
   tls:
      mode: requireTLS
      certificateKeyFile: /etc/ssl/mongodb.pem
      CAFile: /etc/ssl/caToValidateClientCertificates.pem
      CRLFile: /etc/ssl/revokedCertificates.pem
```

Clients that present certificates that are listed in the :file:`/etc/ssl/revokedCertificates.pem` file are not able to connect.

> **Seealso:** You can also configure the revoked certificate list using the
command-line option.
- For :binary:`~bin.mongod`, see :option:`--tlsCRLFile <mongod
  --tlsCRLFile>`.
- For :binary:`~bin.mongos`, see :option:`--tlsCRLFile <mongos
  --tlsCRLFile>`.

Validate Only if a Client Presents a Certificate ````````````````````````````````````````````````

In most cases, it is important to ensure that clients present valid certificates. However, if you have clients that cannot present a client certificate or are transitioning to using a certificate, you may only want to validate certificates from clients that present a certificate.

> **Note:** The procedure uses the `net.tls` settings. For procedures using the
`net.ssl` settings, see `configure-ssl`.

To bypass client certificate validation for clients that do not present a certificate, include :setting:`net.tls.allowConnectionsWithoutCertificates` set to `true`.

For example:

```yaml
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/caToValidateClientCertificates.pem
    allowConnectionsWithoutCertificates: true
```

A :binary:`mongod` / :binary:`mongos` running with these settings allows connection from:

- Clients that do not present a certificate.
- Clients that present a valid certificate.
> **Note:** If the client presents a certificate, the certificate must be a
valid certificate.
All connections, including those that have not presented
certificates, are encrypted using TLS/SSL.

See `ssl-clients` for more information on TLS/SSL connections for clients.

> **Seealso:** You can also configure using the command-line options:
- For :binary:`~bin.mongod`, see
  :option:`--tlsAllowConnectionsWithoutCertificates <mongod
  --tlsAllowConnectionsWithoutCertificates>`.
- For :binary:`~bin.mongos`, see
  :option:`--tlsAllowConnectionsWithoutCertificates <mongos
  --tlsAllowConnectionsWithoutCertificates>`.

### Disallow Protocols

> **Note:** The procedure uses the `net.tls` settings. For procedures using the
`net.ssl` settings, see `configure-ssl`.

To prevent MongoDB servers from accepting incoming connections that use specific protocols, include :setting:`net.tls.disabledProtocols` set to the disallowed protocols.

For example, the following configuration prevents :binary:`mongod` / :binary:`mongos` from accepting incoming connections that use either `TLS1_0` or `TLS1_1`

```yaml
net:
  tls:
    mode: requireTLS
    certificateKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/caToValidateClientCertificates.pem
    disabledProtocols: TLS1_0,TLS1_1
```

> **Seealso:** You can also configure using the command-line options:
- For :binary:`~bin.mongod`, see :option:`--tlsDisabledProtocols
  <mongod --tlsDisabledProtocols>`.
- For :binary:`~bin.mongos`, see :option:`--tlsDisabledProtocols
  <mongos --tlsDisabledProtocols>`.

### TLS/SSL Certificate Passphrase

If the certificate key files for :binary:`mongod` / :binary:`mongos` are encrypted, include :setting:`net.tls.certificateKeyFilePassword` set to the passphrase.

> **Tip:** To avoid specifying the passphrase in cleartext, you can use an
`expansion value <externally-sourced-values>` in the configuration file.

> **Seealso:** You can also configure using the command-line options:
- For :binary:`~bin.mongod`, see :option:`--tlsCertificateKeyFilePassword
  <mongod --tlsCertificateKeyFilePassword>`.
- For :binary:`~bin.mongos`, see :option:`--tlsCertificateKeyFilePassword
  <mongos --tlsCertificateKeyFilePassword>`.

### Online Certificate Rotation

Starting in MongoDB 5.0, you can rotate the following certificate key files on-demand:

- :setting:`TLS Certificates <net.tls.certificateKeyFile>`
- :setting:`CRL (Certificate Revocation List) files <net.tls.CRLFile>`
(on Linux and Windows platforms)

- :setting:`CA (Certificate Authority) files <net.tls.CAFile>`
To rotate one or more of these certificates:

#. Replace the certificate or certificates you wish to rotate on the filesystem, noting the following constraints:

- Each new certificate must have the same filename and
same filepath as the certificate it is replacing.

- If rotating an encrypted :setting:`TLS Certificate
<net.tls.certificateKeyFile>`, its password must be the same as the password for the old certificate (as specified to the :setting:`~net.tls.certificateKeyFilePassword` configuration file setting). Certificate rotation does not support the interactive password prompt.

#. Connect :binary:`~bin.mongosh` to the :binary:`~bin.mongod` or :binary:`~bin.mongos` instance that you wish to perform certificate rotation on.

#. Run the :dbcommand:`rotateCertificates` command or the :method:`db.rotateCertificates()` shell method to rotate the certificates used by the :binary:`~bin.mongod` or :binary:`~bin.mongos` instance.

When certificate rotation takes place:

- Existing connections to the :binary:`~bin.mongod` or
:binary:`~bin.mongos` instance are not terminated, and will continue to use the old certificates.

- Any new connections will use the new certificates.
Incorrect, expired, revoked, or missing certificate files will cause the certificate rotation to fail, but will not invalidate the existing TLS configuration or terminate the running :binary:`~bin.mongod` or :binary:`~bin.mongos` process.

Previous to MongoDB 5.0, certificate rotation required downtime, and was typically performed during maintenance windows.

See :dbcommand:`rotateCertificates` or :method:`db.rotateCertificates()` for additional considerations and full usage instructions.

### Run in FIPS Mode

.. include:: /includes/note-fips-is-enterprise-only.rst

See `/tutorial/configure-fips` for more details.

### Next Steps

To configure TLS/SSL support for clients, see `/tutorial/configure-ssl-clients`.

> **Seealso:** `/tutorial/configure-x509-client-authentication`

## Procedures (Using `net.ssl` Settings)

> **Note:** .. include:: /includes/fact-net-tls-ssl.rst
The procedures in this section use the `net.ssl` settings. For
procedures using the `net.tls` aliases, see `configure-tls`.

### Create a PEM File From Raw Certificate Data

To configure MongoDB with TLS/SSL, you need a single PEM file containing both the private key and the full certificate chain.

If you have raw certificate data, such as a private key `privkey.pem` and a certificate chain file `fullchain.pem`, you can create the required PEM file by concatenating these files:

```sh
cat privkey.pem fullchain.pem > mongodb.pem
```

The resulting `mongodb.pem` file must contain the private key and the certificate chain with their full RFC-7468 encapsulation boundaries, `BEGIN` and `END`.

In your MongoDB configuration, provide the path to the `mongodb.pem` file as the value of the `net.ssl.PEMKeyFile` setting.

Additionally, point the `net.ssl.CAFile` setting to the full chain file `fullchain.pem`, which contains the certificate chain for verifying the client certificate.

### Set Up `mongod` and `mongos` with TLS/SSL Certificate and Key

The following section configures :binary:`mongod` / :binary:`mongos` to use TLS/SSL connections. With these TLS/SSL settings, :binary:`mongod` / :binary:`mongos` presents its certificate key file to the client. However, the :binary:`mongod` / :binary:`mongos` does not require a certificate key file from the client to verify the client's identity. To require client's certificate key file, see `client-cert-validation-ssl` instead.

To use TLS/SSL connections, include the following TLS/SSL settings in your :binary:`mongod` / :binary:`mongos` instance's `configuration file <conf-file>`:

A :binary:`~bin.mongod` instance that uses the above configuration can only accept TLS/SSL connections:

```bash
mongod --config <path/to/configuration/file>
```

See `tls-client-connection-only` for more information on connecting with TLS/SSL.

> **Seealso:** You can also configure :binary:`~bin.mongod` and :binary:`~bin.mongos`
using command-line options instead of the configuration file:
- For :binary:`~bin.mongod`, see `--sslMode`, `--sslPEMKeyFile`,
  and `--sslCertificateSelector`.
- For :binary:`~bin.mongos`, see: `--sslMode`,
  `--sslPEMKeyFile` and `--sslCertificateSelector`.

### Set Up `mongod` and `mongos` with Client Certificate Validation

The following section configures :binary:`mongod` / :binary:`mongos` to use TLS/SSL connections and perform client certificate validation. With these TLS/SSL settings:

- :binary:`mongod` / :binary:`mongos` presents its certificate
key file to the client for verification.

- :binary:`mongod` / :binary:`mongos` requires a certificate
key file from the client to verify the client's identity.

To use TLS/SSL connections, include the following TLS/SSL settings in your :binary:`mongod` / :binary:`mongos` instance's `configuration file <conf-file>`:

> **Note:** You can use system SSL certificate stores for Windows and macOS. To use the
system SSL certificate store, specify `net.ssl.certificateSelector` instead
of specifying the certificate key file.

For example, consider the following `configuration file <conf-file>` for a :binary:`~bin.mongod` instance:

```yaml
net:
   ssl:
      mode: requireSSL
      PEMKeyFile: /etc/ssl/mongodb.pem
      CAFile: /etc/ssl/caToValidateClientCertificates.pem
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
storage:
   dbPath: "/var/lib/mongodb"
processManagement:
   fork: true
net:
   bindIp: localhost,mongodb0.example.net
   port: 27017
```

A :binary:`~bin.mongod` instance that uses the above configuration can only accept TLS/SSL connections and requires a valid certificate from its clients:

```bash
mongod --config <path/to/configuration/file>
```

Clients must specify TLS/SSL connections and present their certificate key file to the instance. See `mongo-connect-require-client-certificates-tls` for more information on connecting with TLS/SSL.

> **Seealso:** You can also configure :binary:`~bin.mongod` and
:binary:`~bin.mongos` using command-line options instead of the
configuration file:
- For :binary:`~bin.mongod`, see `--sslMode`, `--sslPEMKeyFile`, and
  `--sslCAFile`.
- For :binary:`~bin.mongos`, see `--sslMode`, `--sslPEMKeyFile`, and
  `--sslCAFile`.

Block Revoked Certificates for Clients ``````````````````````````````````````

.. include:: /includes/security/block-revoked-certificates-intro.rst

To specify a :abbr:`CRL (Certificate Revocation List)` file, include `net.ssl.CRLFile` set to a file that contains revoked certificates.

For example:

```yaml
net:
   ssl:
      mode: requireSSL
      PEMKeyFile: /etc/ssl/mongodb.pem
      CAFile: /etc/ssl/caToValidateClientCertificates.pem
      CRLFile: /etc/ssl/revokedCertificates.pem
```

Clients that present certificates that are listed in the :file:`/etc/ssl/revokedCertificates.pem` file are not able to connect.

> **Seealso:** You can also configure the revoked certificate list using the command-line option.
- For :binary:`~bin.mongod`, see `--sslCRLFile`.
- For :binary:`~bin.mongos`, see `--sslCRLFile`.

Validate Only if a Client Presents a Certificate ````````````````````````````````````````````````

In most cases, it is important to ensure that clients present valid certificates. However, if you have clients that cannot present a client certificate or are transitioning to using a certificate, you may only want to validate certificates from clients that present a certificate. If the client presents a certificate, the certificate must be a valid certificate. All connections, including those that have not presented certificates, are encrypted using TLS/SSL.

To bypass client certificate validation for clients that do not present a certificate, include `net.ssl.allowConnectionsWithoutCertificates` set to `true`.

For example:

```yaml
net:
  ssl:
    mode: requireSSL
    PEMKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/caToValidateClientCertificates.pem
    allowConnectionsWithoutCertificates: true
```

A :binary:`mongod` / :binary:`mongos` running with these settings allows connection from:

- Clients that do not present a certificate.
- Clients that present a valid certificate.
> **Note:** To use `mongot` with TLS, :setting:`net.tls.allowConnectionsWithoutCertificates`
must be set to `true`. For details, see :setting:`syncSource.replicaSet.tls`.

See `ssl-clients` for more information on TLS/SSL connections for clients.

> **Seealso:** You can also configure using the command-line options:
- For :binary:`~bin.mongod`, see `--sslAllowConnectionsWithoutCertificates`.
- For :binary:`~bin.mongos`, see `--sslAllowConnectionsWithoutCertificates`.

### Disallow Protocols

To prevent MongoDB servers from accepting incoming connections that use specific protocols, include `net.ssl.disabledProtocols` set to the disallowed protocols.

For example, the following configuration prevents :binary:`mongod` / :binary:`mongos` from accepting incoming connections that use either `TLS1_0` or `TLS1_1`

```yaml
net:
  ssl:
    mode: requireSSL
    PEMKeyFile: /etc/ssl/mongodb.pem
    CAFile: /etc/ssl/caToValidateClientCertificates.pem
    disabledProtocols: TLS1_0,TLS1_1
```

> **Seealso:** You can also configure using the command-line options:
- For :binary:`~bin.mongod`, see `--sslDisabledProtocols`.
- For :binary:`~bin.mongos`, see `--sslDisabledProtocols`.

### TLS/SSL Certificate Passphrase

If the certificate key files for :binary:`mongod` / :binary:`mongos` are encrypted, include `net.ssl.PEMKeyPassword` set to the passphrase.

> **Seealso:** You can also configure using the command-line options:
- For :binary:`~bin.mongod`, see `sslPEMKeyPassword`.
- For :binary:`~bin.mongos`, see `--sslPEMKeyPassword`.

### Run in FIPS Mode

.. include:: /includes/note-fips-is-enterprise-only.rst

See `/tutorial/configure-fips` for more details.

### Next Steps

To configure TLS/SSL support for clients, see `/tutorial/configure-ssl-clients`.

> **Seealso:** `/tutorial/configure-x509-client-authentication`
