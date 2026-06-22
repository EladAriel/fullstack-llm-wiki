---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-user-defined-roles.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# User-Defined Roles on Self-Managed Deployments

MongoDB provides a number of `built-in roles </reference/built-in-roles>`. However, if these roles cannot describe the desired set of privileges, you can create new roles.

> **Note:** You can configure custom database roles in the UI for deployments
hosted in {+atlas+}. To learn more, see
:atlas:`Configure Custom Database Roles
</security-add-mongodb-roles>`.

## Role Management Interface

To add a role, MongoDB provides the :method:`db.createRole()` method. MongoDB also provides methods to update existing user-defined roles. For a full list of role management methods, see `role-management-methods`.

## Scope

When adding a role, you create the role in a specific database. MongoDB uses the combination of the database and the role name to uniquely define a role.

.. include:: /includes/fact-roles-privileges-scope.rst

## Centralized Role Data

MongoDB stores all role information in the `system.roles </reference/system-roles-collection>` collection in the `admin` database

Do not access this collection directly but instead use the `role management commands <role-management-commands>` to view and edit custom roles.
