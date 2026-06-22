---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-fips.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# Configure MongoDB for FIPS

## Overview

The Federal Information Processing Standard (FIPS) is a U.S. government computer security standard used to certify software modules and libraries that encrypt and decrypt data securely.  You can configure MongoDB to run with a FIPS 140-2 certified library for OpenSSL. Configure FIPS to run by default or as needed from the command line.

.. include:: /includes/extracts/security-prereq-configure-fips.rst

> **Important:** FIPS is a property of the encryption system and not the access
control system. However, if your environment requires FIPS compliant
encryption and access control, you must ensure that the access
control system uses only FIPS-compliant encryption.
MongoDB's FIPS support covers the way that MongoDB uses SSL/TLS
libraries for network encryption, SCRAM authentication, and X.509
authentication. If you use Kerberos or LDAP authentication, you must
ensure that these external mechanisms are FIPS-compliant.

> **Note:** .. include:: /includes/fact-tls-1.0.rst
.. |binary| replace:: MongoDB

## Platform Support

FIPS mode is only available with MongoDB Enterprise edition. See `/administration/install-enterprise` to download and install MongoDB Enterprise.

FIPS mode is supported on the following platforms:

## OpenSSL3 Support

.. include:: /includes/fact-openssl3-fips-support.rst

## Configuring FIPS

Select the tab below for your platform:

## Additional Considerations

### SCRAM SHA and FIPS Mode

.. include:: /includes/fact-5.1-scram-sha-1-fips-default.rst

.. include:: /includes/fact-tlsFIPSMode_SCRAM-SHA-1.rst

.. include:: /includes/md5-and-scram-sha-1.rst

### `mongod`, `mongos`, and FIPS Mode

If you configure :binary:`~bin.mongod` and :binary:`~bin.mongos` to use FIPS mode, `mongod` and `mongos` use FIPS-compliant connections.

### Database Tools and FIPS Mode

The following programs no longer support the `--sslFIPSMode` option:

- :binary:`~bin.mongodump`
- :binary:`~bin.mongoexport`
- :binary:`~bin.mongofiles`
- :binary:`~bin.mongoimport`
- :binary:`~bin.mongorestore`
- :binary:`~bin.mongostat`
- :binary:`~bin.mongotop`
If you configure :binary:`~bin.mongod` and :binary:`~bin.mongos` to use FIPS mode, the preceding database tools use FIPS-compliant connections automatically.

### MongoDB Shell and FIPS Mode

The default :binary:`~bin.mongosh` distribution:

- Contains OpenSSL 3.
- Uses FIPS-compliant connections to :binary:`~bin.mongod` and
:binary:`~bin.mongos` if you configure `mongod` and `mongos` to use FIPS mode.

MongoDB also provides a MongoDB Shell distribution that can use:

- OpenSSL 1.1 and OpenSSL 3 installed on your server.
- `--tlsFIPSMode` option, which enables the `mongosh` FIPS mode.
> **Seealso:** - To download MongoDB Shell distributions that contain OpenSSL 1.1
  and OpenSSL 3, go to the `MongoDB Download Center
  <https://www.mongodb.com/try/download/shell>`__.
- `mdb-shell-install`
