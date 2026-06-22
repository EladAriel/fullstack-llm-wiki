---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-create-role.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To create a role in a database, you must have:

- the :authaction:`createRole` `action <security-user-actions>` on
that `database resource <resource-specific-db>`.

- the :authaction:`grantRole` `action <security-user-actions>` on
that database to specify privileges for the new role as well as to specify roles to inherit from.

Built-in roles :authrole:`userAdmin` and :authrole:`userAdminAnyDatabase` provide :authaction:`createRole` and :authaction:`grantRole` actions on their respective `resources </reference/resource-document>`.

To create a role with `authenticationRestrictions` specified, you must have the :authaction:`setAuthenticationRestriction` `action <security-user-actions>` on the `database resource <resource-specific-db>` which the role is created.
