---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-create-role.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To create a role in a database, you must have:

- the :authaction:`createRole` `action <security-user-actions>` on
that `database resource <resource-specific-db>`.

- the :authaction:`grantRole` `action <security-user-actions>` on
that database to specify privileges for the new role as well as to specify roles to inherit from.

Built-in roles :authrole:`userAdmin` and :authrole:`userAdminAnyDatabase` provide :authaction:`createRole` and :authaction:`grantRole` actions on their respective `resources </reference/resource-document>`.

To create a role with `authenticationRestrictions` specified, you must have the :authaction:`setAuthenticationRestriction` `action <security-user-actions>` on the `database resource <resource-specific-db>` which the role is created.
