---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-create-user.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- To create a new user in a database, you must have the
:authaction:`createUser` `action <security-user-actions>` on that `database resource <resource-specific-db>`.

- To grant roles to a user, you must have the :authaction:`grantRole`
`action <security-user-actions>` on the role's database.

The :authrole:`userAdmin` and :authrole:`userAdminAnyDatabase` built-in roles provide :authaction:`createUser` and :authaction:`grantRole` actions on their respective `resources <resource-document>`.
