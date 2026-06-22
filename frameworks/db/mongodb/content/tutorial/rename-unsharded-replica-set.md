---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/rename-unsharded-replica-set.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
