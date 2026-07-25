---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-transport-encryption.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# TLS/SSL (Transport Encryption)

## TLS/SSL

.. include:: /includes/tls-ssl-encryption-intro.rst

.. include:: /includes/ssl-and-fips-support.rst

To configure your deployment to use TLS, follow the `quickstart <tls-plan-deployment>`.

### TLS Versions

.. include:: /includes/fact-tls-1.0.rst

### TLS Libraries

.. include:: /includes/fact-tls-libraries.rst

## TLS/SSL Ciphers

MongoDB's TLS/SSL encryption only allows use of strong TLS/SSL ciphers with a minimum of 128-bit key length for all connections.

### Forward Secrecy

Forward Secrecy cipher suites create an ephemeral session key that is protected by the server's private key but is never transmitted. The use of an ephemeral key ensures that even if a server's private key is compromised, you cannot decrypt past sessions with the compromised key.

MongoDB supports Forward Secrecy cipher suites that use Ephemeral Diffie-Hellman (DHE) and Ephemeral Elliptic Curve Diffie-Hellman (ECDHE) algorithms.

Ephemeral Elliptic Curve Diffie-Hellman (ECDHE) ```````````````````````````````````````````````

ECDHE cipher suites are slower than static RSA cipher suites. For better performance with ECDHE, you can use certificates that use Elliptic Curve Digital Signature Algorithm (`ECDSA`). See also `forward-secrecy-performance` for more information.

Ephemeral Diffie-Hellman (DHE) ``````````````````````````````

> **Note:** If clients negotiate a cipher suite with DHE but cannot accept the
server selected parameter, the TLS connection fails.
Strong parameters (i.e. size is greater than 1024) are not supported
with Java 6 and 7 unless extended support has been purchased from
Oracle. However, Java 7 supports and prefers ECDHE, so will
negotiate ECDHE if available.

DHE (and ECDHE) cipher suites are slower performance than static RSA cipher suites, with DHE being significantly slower than ECDHE. See `forward-secrecy-performance` for more information.

Forward Secrecy Performance ```````````````````````````

DHE and ECDHE cipher suites are slower than static RSA cipher suites, with DHE being significantly slower than ECDHE.

For better performance with ECDHE, you can use certificates that use Elliptic Curve Digital Signature Algorithm (`ECDSA`). Alternatively, you can disable ECDHE cipher suites with the :parameter:`opensslCipherConfig` parameter as in the following example (which also disables DHE):

```bash
mongod --setParameter opensslCipherConfig='HIGH:!EXPORT:!aNULL:!kECDHE:!ECDHE:!DHE:!kDHE@STRENGTH'
```

If you need to disable support for DHE cipher suites due to performance, you can use the :parameter:`opensslCipherConfig` parameter, as in the following example:

```bash
mongod --setParameter opensslCipherConfig='HIGH:!EXPORT:!aNULL:!DHE:!kDHE@STRENGTH'
```

## Certificates

To use TLS with MongoDB, you must have TLS certificates. See `tls-certificate-tutorial`.

### Certificate Expiry Warning

.. include:: /includes/extracts/4.4-changes-certificate-expiry-warning.rst

### OCSP (Online Certificate Status Protocol)

.. include:: /includes/fact-ocsp-enabled.rst

To check for certificate revocation, MongoDB :parameter:`enables <ocspEnabled>` the use of OCSP (Online Certificate Status Protocol) by default. The use of OCSP eliminates the need to periodically download a :setting:`Certificate Revocation List (CRL) <net.tls.CRLFile>` and restart the :binary:`mongod` / :binary:`mongos` with the updated CRL.

As part of its OCSP support, MongoDB supports the following on Linux:

.. include:: /includes/list-ocsp-support.rst

MongoDB also provides the following OCSP-related parameters:

.. include:: /includes/list-table-ocsp-parameters.rst

You can set these parameters at startup using the :setting:`setParameter` configuration file setting or the :option:`--setParameter <mongod --setParameter>` command line option.

> **Note:** Starting in MongoDB 5.0, the :dbcommand:`rotateCertificates` command
and :method:`db.rotateCertificates()` method will also refresh any
stapled OCSP responses.

## FIPS Mode

.. include:: /includes/fact-enterprise-only-admonition.rst

The Federal Information Processing Standard (FIPS) is a U.S. government computer security standard used to certify software modules and libraries that encrypt and decrypt data securely. You can configure MongoDB to run with a FIPS 140-2 certified library for OpenSSL. Configure FIPS to run by default or as needed from the command line.

For an example, see `/tutorial/configure-fips`.

## Contents

- Configure mongod & mongos </tutorial/configure-ssl>
- Develop Locally with TLS </tutorial/develop-mongodb-locally-with-tls>
- Configure Clients </tutorial/configure-ssl-clients>
- Upgrade Cluster </tutorial/upgrade-cluster-to-ssl>
- Configure for FIPS </tutorial/configure-fips>
- Plan TLS Deployment </core/tls/plan-tls-deployment>
- Generate Certificates </core/tls/certificate-tutorial>
- Connect Server </core/tls/configure-server-tls-tutorial>
- Connect Client </core/tls/configure-client-tls-tutorial>
