---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/self-managed-user-defined-roles.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

## Prerequisites

.. include:: /includes/access-create-role.rst

To add custom user-defined roles with {+mongosh+}, see the following examples:

- `create-role-to-manage-ops`.
- `create-role-for-mongostat`.
- `create-role-for-system-views`.
## Create a Role to Manage Current Operations

The following example creates a role named `manageOpRole` which provides only the privileges to run both :method:`db.currentOp()` and :method:`db.killOp()`. [#built-in-roles1]_

> **Note:** Users do not need any specific privileges to view or kill their own
operations on :binary:`~bin.mongod` instances. See :method:`db.currentOp()`
and :method:`db.killOp()` for details.

.. include:: /includes/steps/create-role-manage-ops.rst

The built-in role :authrole:`clusterMonitor` also provides the privilege to run :method:`db.currentOp()` along with other privileges, and the built-in role :authrole:`hostManager` provides the privilege to run :method:`db.killOp()` along with other privileges.

## Create a Role to Run `mongostat`

The following example creates a role named `mongostatRole` that provides only the privileges to run :binary:`~bin.mongostat`. [#built-in-roles2]_

.. include:: /includes/steps/create-role-mongostat.rst

:authrole:`clusterMonitor` also provides the privilege to run :binary:`~bin.mongostat` along with other privileges.

## Create a Role to Drop `system.views` Collection across Databases

The following example creates a role named `dropSystemViewsAnyDatabase` that provides the privileges to drop the `system.views` collection in any database.

.. include:: /includes/steps/create-role-dropSystemViews.rst
