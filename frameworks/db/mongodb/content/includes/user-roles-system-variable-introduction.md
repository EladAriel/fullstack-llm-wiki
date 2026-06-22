---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 7.0, you can use the new :variable:`USER_ROLES` system variable to return user `roles <roles>`.

The scenario in this section shows users with various roles who have limited access to documents in a collection containing budget information.

The scenario shows one possible use of `USER_ROLES`. The `budget` collection contains documents with a field named `allowedRoles`. As you'll see in the following scenario, you can write queries that compare the user roles found in the `allowedRoles` field with the roles returned by the `USER_ROLES` system variable.

> **Note:** For another `USER_ROLES` example scenario, see
`create-view-user-roles-system-variable-medical-example`. That
example doesn't store the user roles in the document fields, as is
done in the following example.

For the budget scenario in this section, perform the following steps to create the roles, users, and `budget` collection:
