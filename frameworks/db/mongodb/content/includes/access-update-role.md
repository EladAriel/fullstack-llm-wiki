---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-update-role.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You must have the :authaction:`revokeRole` `action <security-user-actions>` on all databases in order to update a role.

You must have the :authaction:`grantRole` `action <security-user-actions>` on the database of each role in the `roles` array to update the array.

You must have the :authaction:`grantRole` `action <security-user-actions>` on the database of each privilege in the `privileges` array to update the array. If a privilege's resource spans databases, you must have :authaction:`grantRole` on the `admin` database. A privilege spans databases if the privilege is any of the following:

- a collection in all databases
- all collections and all database
- the `cluster` resource
You must have the :authaction:`setAuthenticationRestriction` `action <security-user-actions>` on the database of the target role to update a role's `authenticationRestrictions` document.
