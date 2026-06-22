---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/program/mongokerberos.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# `mongokerberos`

## Synopsis

MongoDB Enterprise provides :binary:`~bin.mongokerberos` for testing MongoDB's Kerberos and GSSAPI `configuration options <security.sasl.options>` against a running Kerberos deployment. :binary:`~bin.mongokerberos` can be used in one of two modes: server and client.

Error messages for both modes include information on specific errors encountered and potential advice for resolving the error.

:binary:`~bin.mongokerberos` supports the following deployment types, in both server and client modes:

- Linux MongoDB clients authenticating to MIT Kerberos deployments on
`supported Linux platforms <prod-notes-supported-platforms>`.

- Windows MongoDB clients authenticating to Windows Active Directory
deployments on `supported Windows platforms <prod-notes-supported-platforms>`.

- Linux MongoDB clients authenticating to Windows Active Directory
deployments.

> **Note:** MongoDB Enterprise and :binary:`~bin.mongokerberos` only support the
[MIT implementation](https://kerberos.org/)_
of Kerberos.

Generally, when configuring options related to `Kerberos authentication <security-kerberos>`, it is good practice to verify your configuration with :binary:`~bin.mongokerberos`.

:binary:`~bin.mongokerberos` is a testing and verification tool; it does not edit any files or configure any services. For configuring Kerberos on your platform please consult the [MIT Kerberos documentation](https://web.mit.edu/kerberos/krb5-latest/doc/)_, or your platform's documentation. For configuring MongoDB to authenticate using Kerberos, please reference the following tutorials:

- `/tutorial/control-access-to-mongodb-with-kerberos-authentication`
- `/tutorial/control-access-to-mongodb-windows-with-kerberos-authentication`.
This document provides a complete overview of all command line options for :binary:`~bin.mongokerberos`.

## Installation

The |tool-binary| tool is part of the MongoDB Database Tools Extra package, and can be `installed with the MongoDB Server <mongokerberos-installed-with-server>` or as a `standalone installation <mongokerberos-standalone-installation>`.

### Install with Server

.. include:: /includes/fact-download-dbtools-extra-server.rst

### Install as Standalone

.. include:: /includes/fact-download-dbtools-extra-standalone.rst

## Usage

:binary:`~bin.mongokerberos` can be run in two modes: server and client.

.. include:: /includes/extracts/require-cmd-line-mongokerberos.rst

### Server Mode

Running :binary:`~bin.mongokerberos` in server mode performs a series of verification steps against your system's Kerberos configuration, including checking for proper DNS resolution, validation of the Kerberos system keytab file, and testing against the MongoDB service principal for your :binary:`~bin.mongod` or :binary:`~bin.mongos` instance.

Before you can use :binary:`~bin.mongokerberos` in server mode, you must:

#. Configure Kerberos on your platform according to your platform's documentation.

#. Create the MongoDB service principal for use with your :binary:`~bin.mongod` or :binary:`~bin.mongos` instance, as described in the following steps:

- `Configure Service Principal on Linux <kerberos-linux-prerequisites>`
- `Configure Service Principal on Windows <assign-service-principal-name>`
Once you have completed these steps, you can run :binary:`~bin.mongokerberos` in server mode using the `--server` flag as follows:

```bash
mongokerberos --server
```

If Kerberos has been configured properly on the server, and the service principal created successfully, the output might resemble the following:

```none
Resolving kerberos environment...
[OK] Kerberos environment resolved without errors.

Verifying DNS resolution works with Kerberos service at <hostname>...
[OK] DNS test successful.

Getting MIT Kerberos KRB5 environment variables...
  * KRB5CCNAME: not set.
  * KRB5_CLIENT_KTNAME: not set.
  * KRB5_CONFIG: not set.
  * KRB5_KTNAME: not set.
  * KRB5_TRACE: not set.
[OK]

Verifying existence of KRB5 keytab FILE:/etc/krb5.keytab...
[OK] KRB5 keytab exists and is populated.

Checking principal(s) in KRB5 keytab...
Found the following principals for MongoDB service mongodb:
  * mongodb/server.example.com@SERVER.EXAMPLE.COM
Found the following kvnos in keytab entries for service mongodb:
  * 3
[OK] KRB5 keytab is valid.

Fetching KRB5 Config...
KRB5 config profile resolved as:
   <Your Kerberos profile file will be output here>
[OK] KRB5 config profile resolved without errors.

Attempting to initiate security context with service credentials...
[OK] Security context initiated successfully.
```

The final message indicates that the system's Kerberos configuration is ready to be used with MongoDB. If any errors are encountered with the configuration, they will be presented as part of the above output.

### Client Mode

Running :binary:`~bin.mongokerberos` in client mode tests authentication against your system's Kerberos environment, performing each step in the Kerberos authentication process, including checking for proper DNS resolution, verification of the Kerberos client keytab file, and testing whether a ticket can be successfully granted. Running :binary:`~bin.mongokerberos` in client mode simulates the client authentication procedure of :binary:`~bin.mongosh`.

Before you can use :binary:`~bin.mongokerberos` in client mode, you must first have configured Kerberos on your platform according to your platform's documentation. Optionally, you may also choose to run :binary:`~bin.mongokerberos` in `server mode <mongokeberos-usage-server>` first to verify that your platform's Kerberos configuration is valid before using client mode.

Once you have completed these steps, you can run :binary:`~bin.mongokerberos` in client mode to test user authentication, using the `--client` flag as follows:

```bash
mongokerberos --client --username <username>
```

You must provide a valid username, which is used to request a Kerberos ticket as part of the authentication procedure. Your platform's Kerberos infrastructure must be aware of this user.

If the provided credentials are valid, and the Kerberos options in the configuration files are valid, the output might resemble the following:

```none
Resolving kerberos environment...
[OK] Kerberos environment resolved without errors.

Verifying DNS resolution works with Kerberos service at <hostname>...
[OK] DNS test successful.

Getting MIT Kerberos KRB5 environment variables...
  * KRB5CCNAME: not set.
  * KRB5_CLIENT_KTNAME: not set.
  * KRB5_CONFIG: not set.
  * KRB5_KTNAME: not set.
  * KRB5_TRACE: not set.
[OK]

Verifying existence of KRB5 client keytab FILE:/path/to/client.keytab...
[OK] KRB5 client keytab exists and is populated.

Checking principal(s) in KRB5 keytab...
[OK] KRB5 keytab is valid.

Fetching KRB5 Config...
KRB5 config profile resolved as:
   <Your Kerberos profile file will be output here>
[OK] KRB5 config profile resolved without errors.

Attempting client half of GSSAPI conversation...
[OK] Client half of GSSAPI conversation completed successfully.
```

The final message indicates that client authentication completed successfully for the user provided.  If any errors are encountered during the authentication steps, they will be presented as part of the above output.

## Options
