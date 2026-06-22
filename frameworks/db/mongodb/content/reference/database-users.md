---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/database-users.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# Database Users

MongoDB uses database users to authenticate clients and grant access to your deployment. Assign `roles <authorization>` to database users based on the level of access and tasks they need to perform.

## Use Cases

Create database users to:

- Allow reads and writes to the database but restrict
administrative access.

- Assign administrative privileges to manage the database, perform
backups, and configure settings.

- Grant read-only access for reporting and analytics.
## Behavior

Roles govern database user permissions. Use MongoDB's `built-in roles <built-in-roles>` or create custom roles.

### Database Users in Self-Managed Deployments

Grant database users in self-managed deployments one or more roles. Roles grant users `privileges <security-user-actions>` to perform actions on specified `resources <resource-document>`.

Users can perform actions on the following resources:

- Collections
- Databases
- Clusters
To create and manage users in your self-managed deployment, use the :dbcommand:`createUser` command or the :method:`db.createUser()` method.

### Database Users in {+atlas+}

Database users in {+atlas+} have different built-in roles than self-managed deployments. When you create a database user in {+atlas+}, Atlas built-in roles apply to all databases in your project.

> **Note:** Database users are separate from Atlas users. Database users
access MongoDB databases. Atlas users access the Atlas
application.

Create database users, assign built-in roles, and create custom roles in the :atlascli:`{+atlas-cli+} </install-atlas-cli/>`, `atlas-admin-api-overview`, or the `Atlas UI <atlas-ui>`. To learn more, see :atlas:`Add Database Users </security-add-mongodb-users/#add-database-users>`.

## Get Started

To create and manage database users, see:

- `manage-users-and-roles`.
- `Configure Database Users on Atlas <mongodb-users>`.
## Details

### Authentication

Specify the authentication mechanism when you create a user. MongoDB supports the following authentication mechanisms:

.. include:: /includes/fact-authentication-compat-table.rst

To learn more, see:

- `authentication`
- :atlas:`Configure Cluster Authentication and Authorization on
Atlas </security/config-db-auth/>`

### Authorization

MongoDB uses Role-Based Access Control to verify user access to resources and operations. Database users in {+atlas+} have different built-in roles than self-hosted deployments. However, MongoDB builds all built-in roles from the same set of `privilege actions <security-user-actions>`.

To learn more, see:

- `authorization`
- :ref:`Built-In Roles and Privileges on Atlas
<mongodb-users-roles-and-privileges>`

## Contents

- Built-In Roles </reference/built-in-roles>
- Privilege Actions </reference/privilege-actions>
- Non-Root User Permissions </reference/non-root-user-permissions>
