---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/rename-unsharded-replica-set.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# Rename a Self-Managed Replica Set

To rename a MongoDB replica set, you must shut down all members of the replica set, then configure each member's `local` database with the new replica set name.

This procedure requires downtime.

## Prerequisites

- Ensure that your replica set is not sharded. The renaming procedure
is for unsharded replica sets only.

- Before renaming a replica set, perform a full
`backup of your MongoDB deployment <backup-methods>`.

- When `authentication <authentication>` is enabled, ensure that
your `user role <roles>` has `find`, `insert`, and `remove` privileges on the `system.replset` collection in each member's `local` database.

> **Tip:**  You can view the privileges for a role by issuing the :dbcommand:`rolesInfo`
 command with the `showPrivileges` and `showBuiltinRoles` fields both set to `true`.

## Procedure

.. include:: /includes/steps/rename-unsharded-replica-set.rst
