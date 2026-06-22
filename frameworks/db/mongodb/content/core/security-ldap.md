---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-ldap.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Self-Managed LDAP Proxy Authentication

[MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced) supports proxying authentication requests to a Lightweight Directory Access Protocol (LDAP) service.

MongoDB supports simple and SASL binding to LDAP servers:

## Considerations

A full description of LDAP is beyond the scope of this documentation. This page assumes prior knowledge of LDAP.

This documentation only describes MongoDB LDAP authentication, and does not replace other resources on LDAP. We encourage you to thoroughly familiarize yourself with LDAP and its related subject matter before configuring LDAP authentication.

MongoDB can provide [professional services](https://www.mongodb.com/products/consulting) for optimal configuration of LDAP authentication for your MongoDB deployment.

### Connection Pool

When connecting to the LDAP server for authentication/authorization, MongoDB, by default:

- Uses connection pooling if run:
- on Windows or
- on Linux where MongoDB Enterprise binaries are linked against
`libldap_r <libldap-vs-libldap_r>`.

- Does not use connection pooling if run:
- on Linux where MongoDB Enterprise binaries are linked against
`libldap <libldap-vs-libldap_r>`.

To change the connection pooling behavior, update the :parameter:`ldapUseConnectionPool` parameter.

### `saslauthd` and Directory Permissions

.. include:: /includes/fact-saslauthd-permission.rst

### `libldap` and `libldap_r`

.. include:: /includes/extracts/4.2-changes-libldap.rst

### Managing LDAP Users on the MongoDB server

When using LDAP authentication **without** `LDAP authorization <ldap-authorization>`, user management requires managing users both on the LDAP server and the MongoDB server. For each user authenticating via LDAP, MongoDB requires a user on the `$external` database whose name exactly matches the authentication username. Changes to a user on the LDAP server may require changes to the corresponding MongoDB `$external` user.

.. include:: /includes/extracts/sessions-external-username-limit.rst

To manage users on the MongoDB server, you must authenticate as an LDAP user whose corresponding MongoDB `$external` user has user administrative privileges on the `$external` database, such as those provided by :authrole:`userAdmin`.

> **Important:** If no `$external` users have user administrative privileges on
`$external` database, you cannot perform user management for LDAP
authentication. This scenario may occur if you configure users prior to
enabling LDAP authentication, but do not create the appropriate user
administrators.

### Managing existing non-LDAP users

If there are existing users not on the `$external` database, you must meet the following requirements for each user to ensure continued access:

- User has a corresponding user object on the LDAP server
- User exists on the `$external` database with equivalent roles and
privileges

If you want to continue allowing access by users not on the `$external` database, you must configure :setting:`setParameter` :parameter:`authenticationMechanisms` to include `SCRAM-SHA-1` and/or `SCRAM-SHA-256` as appropriate. Users must then specify `--authenticationMechanism SCRAM-SHA-1` or `SCRAM-SHA-256` when authenticating.

### Deploying LDAP authentication on a replica set

For `replica sets <replica set>`, configure LDAP authentication on `secondary` and `arbiter` members first before configuring the `primary`. This also applies to `shard replica sets <shards-concepts>`, or `config server replica sets <csrs>`. Configure one replica set member at a time to maintain a majority of members for write availability.

### Deploying LDAP authentication on a sharded cluster

In `sharded clusters <sharded cluster>`, you must configure LDAP authentication on the `config servers <config server>` and each :binary:`~bin.mongos` for cluster-level users. You can optionally configure LDAP authorization on each `shard` for shard-local users.

## LDAP Authentication via the Operating System LDAP libraries

The LDAP authentication via OS libraries process is summarized below:

#. A client authenticates to MongoDB, providing a user's credentials.

#. If the username requires mapping to an LDAP DN prior to binding against the LDAP server, MongoDB can apply transformations based on the configured :setting:`security.ldap.userToDNMapping` setting.

#. MongoDB binds to an LDAP server specified in :setting:`security.ldap.servers` using the provided username or, if a transformation was applied, the transformed username.

MongoDB uses simple binding by default, but can also use `sasl` binding if configured in :setting:`security.ldap.bind.method` and :setting:`security.ldap.bind.saslMechanisms`.

If a transformation requires querying the LDAP server, or if the LDAP server disallows anonymous binds, MongoDB uses the username and password specified to :setting:`security.ldap.bind.queryUser` and :setting:`security.ldap.bind.queryPassword` to bind to the LDAP server before attempting to authenticate the provided user credentials.

#. The LDAP server returns the result of the bind attempt to MongoDB. On success, MongoDB attempts to authorize the user.

#. The MongoDB server attempts to map the username to a user on the `$external` database, assigning the user any roles or privileges associated to a matching user. If MongoDB cannot find a matching user, authentication fails.

#. The client can perform those actions for which MongoDB granted the authenticated user roles or privileges.

To use LDAP for authentication via operating system libraries, specify the following settings as a part of your :binary:`~bin.mongod` or :binary:`~bin.mongos` configuration file:

## LDAP Authentication via `saslauthd`

> **Warning:** .. include:: /includes/admonition-mongodb-enterprise-windows-ldap.rst

### Considerations

.. include:: /includes/admonition-saslauthd-ldap-considerations.rst

### Configuration

To configure the MongoDB server to bind to the LDAP server using via `saslauthd`, start the :binary:`~bin.mongod` using either the following command line options or the following configuration file settings:

You need to create or update the `saslauthd.conf` file with the parameters appropriate for your LDAP server. Documenting `saslauthd.conf` is out of scope for this documentation.

.. include:: /includes/fact-saslauthd-permission.rst

The following tutorials provide basic information on configuring `saslauthd.conf` to work with two popular LDAP services:

- `/tutorial/configure-ldap-sasl-openldap`
- `/tutorial/configure-ldap-sasl-activedirectory`
Please see the documentation for `saslauthd` as well as your specific LDAP service for guidance.

## Connect to a MongoDB server via LDAP authentication

To authenticate to a MongoDB server via LDAP authentication, use :method:`db.auth()` on the `$external` database with the following parameters:

## Contents

- Use ActiveDirectory </tutorial/configure-ldap-sasl-activedirectory>
- Use OpenLDAP </tutorial/configure-ldap-sasl-openldap>
- Use Native LDAP </tutorial/authenticate-nativeldap-activedirectory>
