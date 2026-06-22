---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/authorization.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================================

# Role-Based Access Control in Self-Managed Deployments

MongoDB employs Role-Based Access Control (RBAC) to govern access to a MongoDB system. A user is granted one or more `roles <roles>` that determine the user's access to database resources and operations. Outside of role assignments, the user has no access to the system.

## Enable Access Control

MongoDB does not enable access control by default. You can enable authorization using the :option:`--auth <mongod --auth>` or the :setting:`security.authorization` setting. Enabling `internal authentication </core/security-internal-authentication>` also enables client authorization. Once access control is enabled, users must `authenticate <authentication>` themselves.

## Roles

A role grants privileges to perform the specified `actions <security-user-actions>` on a `resource </reference/resource-document>`. Each privilege is either specified explicitly in the role or inherited from another role or both.

### Access

Roles never limit privileges. If a user has two roles, the role with the greater access takes precedence.

For example, if you grant the :authrole:`read` role on a database to a user that already has the :authrole:`readWriteAnyDatabase` role, the `read` grant does **not** revoke write access on the database.

To revoke a role from a user, use the :dbcommand:`revokeRolesFromUser` command.

### Authentication Restrictions

Roles can impose authentication restrictions on users, requiring them to connect from specified source and destination IP address ranges.

For more information, see `create-role-auth-restrictions`.

### Privileges

A privilege consists of a specified resource and the actions permitted on the resource.

A `resource <resource-document>` is a database, collection, set of collections, or the cluster. If the resource is the cluster, the affiliated actions affect the state of the system rather than a specific database or collection. For information on the resource documents, see `/reference/resource-document`.

An `action <security-user-actions>` specifies the operation allowed on the resource. For available actions see `/reference/privilege-actions`.

### Inherited Privileges

A role can include one or more existing roles in its definition, in which case the role inherits all the privileges of the included roles.

A role can inherit privileges from other roles in its database. A role created on the `admin` database can inherit privileges from roles in any database.

### View Role's Privileges

You can view the privileges for a role by issuing the :dbcommand:`rolesInfo` command with the `showPrivileges` and `showBuiltinRoles` fields both set to `true`.

## Users and Roles

Assign roles when you create users or update existing users to grant or revoke roles. To list all user management methods, see `user-management-methods`

A user assigned a role receives all the privileges of that role. A user can have multiple roles. By assigning to the user roles in various databases, a user created in one database can have permissions to act on other databases.

> **Note:** The first user created in the database must be a user administrator
who has the privileges to manage other users. See
`/tutorial/enable-authentication`.

## Built-In Roles and User-Defined Roles

MongoDB provides `built-in roles <built-in-roles>` that provide a set of privileges commonly needed in a database system.

If these built-in roles cannot provide the desired set of privileges, you can create and modify `user-defined roles </core/security-user-defined-roles>`.

## LDAP Authorization

.. include:: /includes/LDAP-deprecated.rst

MongoDB Enterprise supports querying an LDAP server for the LDAP groups the authenticated user is a member of. MongoDB maps the Distinguished Names (DN) of each returned group to `roles <roles>` on the `admin` database. MongoDB authorizes the user based on the mapped roles and their associated privileges. See `LDAP Authorization <security-ldap-external>` for more information.

## Contents

- User Defined Roles </core/security-user-defined-roles>
- Manage Users & Roles </tutorial/manage-users-and-roles>
- Change Password & Custom Data </tutorial/change-own-password-and-custom-data>
- Collection-Level Access </core/collection-level-access-control>
- LDAP Authorization </core/security-ldap-external>
- LDAP Deprecation </core/LDAP-deprecation>
