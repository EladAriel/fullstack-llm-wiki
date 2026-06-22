---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/program/mongoldap.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============

# `mongoldap`

MongoDB Enterprise

.. include:: /includes/LDAP-deprecated.rst

## Synopsis

MongoDB Enterprise provides :binary:`~bin.mongoldap` for testing MongoDB's LDAP `configuration options <security.ldap.options>` against a running LDAP server or set of servers.

To validate the LDAP options in the configuration file, set the :binary:`~bin.mongoldap` :option:`--config <mongoldap --config>` option to the configuration file's path.

To test the LDAP configuration options, you must specify a :option:`--user <mongoldap --user>` and `--password`. :binary:`~bin.mongoldap` simulates authentication to a MongoDB server running with the provided configuration options and credentials.

:binary:`~bin.mongoldap` returns a report that includes the success or failure of any step in the LDAP authentication or authorization procedure. Error messages include information on specific errors encountered and potential advice for resolving the error.

When configuring options related to `LDAP authorization <security-ldap-external>`, :binary:`~bin.mongoldap` executes an LDAP query constructed using the provided configuration options and username, and returns a list of roles on the `admin` database which the user is authorized for.

You can use this information when configuring `LDAP authorization roles <security-ldap-external-roles>` for user access control. For example, use :binary:`~bin.mongoldap` to ensure your configuration allows privileged users to gain the necessary roles to perform their expected tasks. Similarly, use :binary:`~bin.mongoldap` to ensure your configuration disallows non-privileged users from gaining roles for accessing the MongoDB server, or performing unauthorized actions.

When configuring options related to `LDAP authentication <security-ldap>`, use :binary:`~bin.mongoldap` to ensure that the authentication operation works as expected.

.. include:: /includes/extracts/require-cmd-line-mongoldap.rst

This document provides a complete overview of all command line options for :binary:`~bin.mongoldap`.

## Installation

The |tool-binary| tool is part of the MongoDB Database Tools Extra package, and can be `installed with the MongoDB Server <mongoldap-installed-with-server>` or as a `standalone installation <mongoldap-standalone-installation>`.

### Install with Server

.. include:: /includes/fact-download-dbtools-extra-server.rst

### Install as Standalone

.. include:: /includes/fact-download-dbtools-extra-standalone.rst

## Usage

> **Note:** A full description of LDAP or Active Directory is beyond the scope of
this documentation.

Consider the following sample configuration file, designed to support LDAP authentication and authorization via Active Directory:

```yaml
security:
   authorization: "enabled"
   ldap:
      servers: "activedirectory.example.net"
      bind:
         queryUser: "mongodbadmin@dba.example.com"
         queryPassword: "secret123"
      userToDNMapping:
         '[
            {
               match : "(.+)",
               ldapQuery: "DC=example,DC=com??sub?(userPrincipalName={0})"
            }
         ]'
      authz:
         queryTemplate: "DC=example,DC=com??sub?(&(objectClass=group)(member:1.2.840.113556.1.4.1941:={USER}))"
setParameter:
   authenticationMechanisms: "PLAIN"
```

You can use :binary:`~bin.mongoldap` to validate the configuration file, which returns a report of the procedure. You must specify a username and password for :binary:`~bin.mongoldap`.

```bash
mongoldap --config=<path-to-config> --user="bob@dba.example.com" --password="secret123" 
```

If the provided credentials are valid, and the LDAP options in the configuration files are valid, the output might be as follows:

```bash
Checking that an LDAP server has been specified...
[OK] LDAP server found

Connecting to LDAP server...
[OK] Connected to LDAP server

Parsing MongoDB to LDAP DN mappings..
[OK] MongoDB to LDAP DN mappings appear to be valid

Attempting to authenticate against the LDAP server...
[OK] Successful authentication performed

Checking if LDAP authorization has been enabled by configuration...
[OK] LDAP authorization enabled

Parsing LDAP query template..
[OK] LDAP query configuration template appears valid

Executing query against LDAP server...
[OK] Successfully acquired the following roles:
...
```

## Behavior

Starting in MongoDB 5.1, `mongoldap` supports prefixing LDAP server with `srv:` and `srv_raw:`.

.. include:: /includes/ldap-srv-details.rst

## Options

.. include:: /includes/query-password.rst
