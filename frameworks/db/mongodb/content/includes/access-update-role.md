---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-update-role.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You must have the :authaction:`revokeRole` `action <security-user-actions>` on all databases in order to update a role.

You must have the :authaction:`grantRole` `action <security-user-actions>` on the database of each role in the `roles` array to update the array.

You must have the :authaction:`grantRole` `action <security-user-actions>` on the database of each privilege in the `privileges` array to update the array. If a privilege's resource spans databases, you must have :authaction:`grantRole` on the `admin` database. A privilege spans databases if the privilege is any of the following:

- a collection in all databases
- all collections and all database
- the `cluster` resource
You must have the :authaction:`setAuthenticationRestriction` `action <security-user-actions>` on the database of the target role to update a role's `authenticationRestrictions` document.
