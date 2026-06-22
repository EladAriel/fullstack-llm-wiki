---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-users.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# Users in Self-Managed Deployments

To authenticate a client in MongoDB, you must add a corresponding user to MongoDB.

## User Management

You can add a user with the :method:`db.createUser()` method using :binary:`~bin.mongosh`. The first user you create must have privileges to create other users. The :authrole:`userAdmin` or :authrole:`userAdminAnyDatabase` role both confer the privilege to create other users.

> **Seealso:** `/tutorial/create-users`

You can grant a user privileges by assigning `roles </core/authorization>` to the user when you create the user. You can also grant or revoke roles and update passwords by updating existing users. For a full list of user management methods, see `user-management-methods`.

> **Seealso:** `/tutorial/manage-users-and-roles`

## Authentication Database

The database where you add a user is its authentication database.

A user's privileges are not limited to their authentication database and can span multiple databases. For more information on roles, see `/core/authorization`.

A user's name and authentication database serve as a unique identifier for that user. MongoDB associates a user with a unique `userId` upon creation in MongoDB. However, `LDAP managed users <security-ldap>` created on an LDAP server do not have an associated document in the `system.users <system-users>` collection, and therefore don't have a `admin.system.users.userId` field associated with them.

If two users have the same name but are created in different databases, they are two separate users. If you want to have a single user with permissions on multiple databases, create a single user with a role for each applicable database.

## Centralized User Data

MongoDB stores all user information, including `name <admin.system.users.user>`, `password <admin.system.users.credentials>`, and the user's `authentication database <admin.system.users.db>`, in the `system.users </reference/system-users-collection>` collection in the `admin` database.

Do not modify this collection directly. To manage users, use the designated `user management commands <user-management-commands>`.

## Sharded Cluster Users

To create users for a sharded cluster, connect to a :binary:`~bin.mongos` instance and add the users. To authenticate as a user created on a :binary:`~bin.mongos` instance, you must authenticate through a :binary:`~bin.mongos` instance.

In sharded clusters, MongoDB stores user configuration data in the `admin` database of the `config servers <config server>`.

### Shard Local Users

Some maintenance operations, such as :dbcommand:`compact` or :method:`rs.reconfig()`, require direct connections to specific shards in a sharded cluster. To perform these operations, you must connect directly to the shard and authenticate as a shard local administrative user.

To create a shard local administrative user, connect directly to the primary of the shard and create the user. For instructions on how to create a shard local user administrator see the `/tutorial/deploy-sharded-cluster-with-keyfile-access-control` tutorial.

MongoDB stores shard local users in the `admin` database of the shard itself. These shard local users are independent from the users added to the sharded cluster through a :binary:`~bin.mongos`. Shard local users are local to the shard and are inaccessible by :binary:`~bin.mongos`.

.. include:: /includes/dSO-role-intro.rst

Direct connections to a shard should only be used for shard-specific maintenance and configuration. In general, clients must connect to the sharded cluster through the :binary:`~bin.mongos`.

.. include:: /includes/dSO-warning.rst

## Contents

- Create </tutorial/create-users>
- Authenticate </tutorial/authenticate-a-user>
- List </tutorial/list-users>
