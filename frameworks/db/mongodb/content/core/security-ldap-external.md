---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-ldap-external.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# LDAP Authorization on Self-Managed Deployments

.. include:: /includes/LDAP-deprecated.rst

[MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced) supports querying an LDAP server for the LDAP groups to which the authenticated user belongs. MongoDB maps the distinguished names (DN) of each returned group to `roles <roles>` on the `admin` database. MongoDB authorizes the user based on the mapped roles and their associated privileges.

The LDAP Authorization process is summarized below:

#. A client connects to MongoDB and performs authentication with any `authentication <authentication>` mechanism that `supports external authentication <security-ldap-external-compatibility>`.

.. include:: /includes/extracts/sessions-external-username-limit.rst

#. MongoDB binds to the LDAP server specified with :setting:`security.ldap.servers` using the credentials specified with :setting:`security.ldap.bind.queryUser` and :setting:`security.ldap.bind.queryPassword`.

MongoDB uses simple binding by default, but can use `sasl` binding instead if configured in :setting:`security.ldap.bind.method` and :setting:`security.ldap.bind.saslMechanisms`.

#. MongoDB constructs an LDAP query using the :setting:`security.ldap.authz.queryTemplate` and queries the LDAP server for the authenticated user's group membership.

MongoDB can use the :setting:`security.ldap.userToDNMapping` option to transform the username for supporting the query template.

#. The LDAP server evaluates the query and returns the list of groups to which the authenticated user belongs.

#. MongoDB authorizes the user to perform actions on the server by mapping each returned group's Distinguished Name (DN) into a `role <authorization>` on the `admin` database. If a returned group DN exactly matches the name of an existing role on the `admin` database, MongoDB grants the user the roles and privileges assigned to that role. See `security-ldap-external-roles` for more information.

#. The client can perform actions on the MongoDB server which require the roles or privileges granted to the authenticated user.

#. At an interval defined by :parameter:`ldapUserCacheInvalidationInterval`, MongoDB flushes the `$external` cache. Prior to executing subsequent operations performed by externally authorized users, MongoDB re-acquires their group membership from the LDAP server.

## Considerations

A full description of LDAP is beyond the scope of this documentation. This page assumes prior knowledge of LDAP.

This documentation only describes MongoDB LDAP authorization, and does not replace other resources on LDAP. We encourage you to thoroughly familiarize yourself with LDAP and its related subject matter before configuring LDAP authentication.

MongoDB can provide [professional services](https://www.mongodb.com/products/consulting) for optimal configuration of LDAP authorization for your MongoDB deployment.

### Compatible Authentication Mechanism

MongoDB supports LDAP authorization with the following authentication methods:

- `security-ldap`
- `security-kerberos`
- `security-auth-x509`
With this configuration, MongoDB uses LDAP, X.509, or Kerberos authorization to authenticate client connections.

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

### `libldap` and `libldap_r`

.. include:: /includes/extracts/4.2-changes-libldap.rst

### User Management

With LDAP authorization, user creation and management occurs on the LDAP server. MongoDB requires creation of `roles <roles>` on the `admin` database, with the name of each role exactly matching a LDAP group Distinguished Name (DN). This is in contrast to MongoDB managed authorization, which requires creating users on the `$external` database.

To manage roles on the MongoDB server, authenticate as a user whose group membership corresponds to a `admin` database role with role administration privileges, such as those provided by :authrole:`userAdmin`. Create or update roles corresponding to LDAP group DNs such that users with membership in that group receive the appropriate roles and privileges.

For example, an LDAP group for database administrators might have a role with administrative roles and privileges. An LDAP group for marketing or analytics users may have a role with only have read privileges on certain databases.

> **Important:** When configuring a role for a corresponding LDAP Group, remember that all
users with membership in that group can receive the configured roles and
privileges. Consider applying the principle of least privilege when
configuring MongoDB roles, LDAP groups, or group membership.

If no role with role administration privileges exists AND no non-`$external` user with these privileges exists, you effectively cannot perform user management, as no new or existing roles can be altered to reflect additions or changes to groups or group membership on the LDAP server.

To remedy a scenario where you cannot manage roles on the MongoDB server, perform the following procedure:

#. Restart the MongoDB server without authentication and LDAP authorization

#. Create a role on the `admin` database whose name corresponds to the appropriate LDAP group Distinguished Name. When choosing a group DN, consider which group is most appropriate for database administration.

#. Restart the MongoDB server with authentication and LDAP authorization

#. Authenticate as a user with membership in the group corresponding to the created administrative role.

### Existing Users

A MongoDB server using LDAP for authorization makes any existing users on the `$external` database inaccessible. If there are existing users in `$external` database, you must meet the following requirements for each user on the `$external` database to ensure continued access:

- User has a corresponding user object on the LDAP server
- User object has membership in the appropriate LDAP groups
- MongoDB has roles on the `admin` database named for the user's LDAP
groups, such that the granted roles and privileges are identical to those granted to the non-`$external` user.

If you want to continue allowing access by users not on the `$external` database, ensure the :parameter:`authenticationMechanisms` parameter includes `SCRAM-SHA-1` and/or `SCRAM-SHA-256` as appropriate. Alternatively, apply the requirements listed above for transitioning those users to LDAP authorization.

### Replica Sets

For `replica sets <replica set>`, configure LDAP authorization on the `secondary` and `arbiter` members first before configuring the `primary`. This also applies to `shard replica sets <shards-concepts>`, or `config server replica sets <csrs>`. Configure one replica set member at a time to maintain a majority of members for write availability.

### Sharded Clusters

In `sharded clusters <sharded cluster>`, you must configure LDAP authorization on the `config servers <config server>` for cluster-level users. You can optionally configure LDAP authorization on each `shard` for shard-local users.

## Configuration

You must configure the following settings to use LDAP Authorization:

To use LDAP for authorization via operating system libraries, specify the following settings as a part of your :binary:`~bin.mongod` or :binary:`~bin.mongos` configuration file:

When you have configured LDAP authorization, restart :program:`mongod` or :program:`mongos`. The server now uses LDAP authorization with X.509, Kerberos, or LDAP to authenticate client connections.

### LDAP Query Template

MongoDB uses the :setting:`security.ldap.authz.queryTemplate` to create an [RFC4516](https://tools.ietf.org/html/rfc4516) formatted LDAP query URL. In the template, you can use either:

- `{USER}` placeholder to substitute the authenticated username into
the LDAP query URL. If MongoDB transformed the username using :setting:`~security.ldap.userToDNMapping`, MongoDB replaces the `{USER}` token with the transformed username when constructing the LDAP query URL.

- `{PROVIDED_USER}` placeholder to substitute the supplied username,
i.e. before either authentication or LDAP transformation, into the LDAP query.

Design the query template to retrieve the user's groups.

The LDAP query URL must conform to the format defined in [RFC4516](https://tools.ietf.org/html/rfc4516):

```text
[ dn  [ ? [attributes] [ ? [scope] [ ? [filter] [ ? [Extensions] ] ] ] ] ]
```

Consider the definition of each component, as quoted from RFC4516:

If the query includes an `attribute`, MongoDB assumes the query retrieves a the DNs which this entity is member of.

If the query does not include an attribute, MongoDB assumes the query retrieves all entities for which the user is member of.

MongoDB currently ignores any extensions specified in the LDAP query.

> **Important:** A full description of RFC4516 or LDAP query URL construction is out of
scope for this documentation.

## Tutorials

The following tutorials contain procedures for connecting to an LDAP server via the Operating System LDAP libraries:

- `/tutorial/authenticate-nativeldap-activedirectory`
- `/tutorial/kerberos-auth-activedirectory-authz`
## Connecting to a MongoDB server using LDAP Authorization

When using LDAP for authorization, users connecting via :binary:`~bin.mongosh` must:

- set :option:`--authenticationDatabase <mongosh --authenticationDatabase>` to `$external`.
- set :option:`--authenticationMechanism <mongosh --authenticationMechanism>` to the appropriate authentication
mechanism.

If using `LDAP authentication <security-ldap>`, set this to `PLAIN`.

If using `Kerberos authentication <security-kerberos>`, set this to `GSSAPI`.

If using `X.509 <security-auth-x509>`, set this to `MONGODB-X.509`.

- set :option:`--username <mongosh --username>` to a username that respects the
:setting:`security.ldap.authz.queryTemplate`, or any configured :setting:`security.ldap.userToDNMapping` template.

- set :option:`--password <mongosh --password>` to the appropriate password.
Include the :option:`--host <mongosh --host>` and :option:`--port <mongosh --port>` of the MongoDB server, along with any other options relevant to your deployment.

For example, the following operation authenticates to a MongoDB server running with LDAP authentication and authorization:

```bash
mongosh --username alice@dba.example.com --password  --authenticationDatabase '$external' --authenticationMechanism "PLAIN"  --host "mongodb.example.com" --port 27017
```

If you do not specify the password to the :option:`--password <mongosh --password>` command-line option, :binary:`~bin.mongosh` prompts for the password.

> **Important:** The `$external` argument must be placed in single quotes, not
double quotes, to prevent the shell from interpreting `$external`
as a variable.

## MongoDB Roles for LDAP Authorization

MongoDB maps each returned group distinguished name (DN) returned by the LDAP :setting:`query <security.ldap.authz.queryTemplate>` to a `role <authorization>` on the `admin` database.

If MongoDB acquires a group whose DN **exactly** matches the name of an existing role, MongoDB grants the authenticated user roles and `privileges <privileges>` associated with that role. If MongoDB cannot map any of the returned groups to a role, MongoDB grants no privileges to the user.

> **Note:** `LDAP <security-ldap>` and `kerberos <security-kerberos>`
authentication normally require creating users in the `$external`
database. If you also use LDAP for authorization, you do not need to
create users in the `$external` database. You only need to create the
appropriate roles in the `admin` database. Users still authenticate
against the `$external` database.

> **Important:** If you are using LDAP for authorization and your LDAP group DNs
contain [RFC4514](https://tools.ietf.org/html/rfc4514) escaped
sequences, the roles you create in the `admin` database must also
be escaped following RFC4514.
