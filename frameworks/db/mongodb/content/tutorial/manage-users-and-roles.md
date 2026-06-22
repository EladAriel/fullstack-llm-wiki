---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/manage-users-and-roles.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# Manage Users and Roles on Self-Managed Deployments

The following examples cover user and role management under the MongoDB authorization model for self-managed deployments. To create a user, see `create-users`.

## Prerequisites

If you have `enabled access control <enable-access-control>` for your deployment, you must authenticate as a user with the required privileges specified in each section. To perform the operations listed in this tutorial, user administrators require the :authrole:`userAdminAnyDatabase` role, or :authrole:`userAdmin` role in the specific databases. For details on adding a user administrator as the first user, see `<enable-access-control>`

## Create a User-Defined Role

> **Note:** To create user-defined roles in {+atlas+}, see
`add-mongodb-roles` in the {+atlas+} documentation.

MongoDB provides `built-in roles <built-in-roles>` for common access patterns. If built-in roles don't cover your required privileges, create a user-defined role.

.. include:: /includes/fact-roles-privileges-scope.rst

To create a new role, use the :method:`db.createRole()` method, specifying the privileges in the `privileges` array and the inherited roles in the `roles` array.

MongoDB uses the combination of the database name and the role name to uniquely define a role. Each role is scoped to the database in which you create the role, but MongoDB stores all role information in the `admin.system.roles` collection in the `admin` database.

.. include:: /includes/self-managed-user-defined-roles.rst

## Modify Access for an Existing User

> **Note:** To modify an existing database user's roles in {+atlas+},
see `<modify-mongodb-users>` in the {+atlas+} documentation.

### Prerequisites

- .. include:: /includes/access-grant-roles.rst
- .. include:: /includes/access-revoke-roles.rst
- .. include:: /includes/access-roles-info.rst
### Procedure

.. include:: /includes/steps/change-user-privileges.rst

## Modify the Password for an Existing User

> **Note:** To modify an existing {+atlas+} user's password, see
`<modify-mongodb-users>` in the {+atlas+} documentation.

### Prerequisites

.. include:: /includes/access-change-password.rst

### Procedure

.. include:: /includes/steps/change-user-password.rst

> **Seealso:** `<change-password-custom-data>`

## View a User's Roles

> **Note:** To view a user's roles in {+atlas+}, see
`<view-mongodb-users>` in the {+atlas+}
documentation.

### Prerequisites

.. include:: /includes/access-user-info.rst

### Procedure

.. include:: /includes/steps/verify-user-privileges.rst

## View a Role's Privileges

> **Note:** To view a role's privileges in {+atlas+}, see
`<view-mongodb-roles>` in the {+atlas+} documentation.

### Prerequisites

.. include:: /includes/access-roles-info.rst

### Procedure

.. include:: /includes/steps/view-role-info.rst
