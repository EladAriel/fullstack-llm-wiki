---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-create-user.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- To create a new user in a database, you must have the
:authaction:`createUser` `action <security-user-actions>` on that `database resource <resource-specific-db>`.

- To grant roles to a user, you must have the :authaction:`grantRole`
`action <security-user-actions>` on the role's database.

The :authrole:`userAdmin` and :authrole:`userAdminAnyDatabase` built-in roles provide :authaction:`createUser` and :authaction:`grantRole` actions on their respective `resources <resource-document>`.
