---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-introduction.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 7.0, you can use the new :variable:`USER_ROLES` system variable to return user `roles <roles>`.

The scenario in this section shows users with various roles who have limited access to documents in a collection containing budget information.

The scenario shows one possible use of `USER_ROLES`. The `budget` collection contains documents with a field named `allowedRoles`. As you'll see in the following scenario, you can write queries that compare the user roles found in the `allowedRoles` field with the roles returned by the `USER_ROLES` system variable.

> **Note:** For another `USER_ROLES` example scenario, see
`create-view-user-roles-system-variable-medical-example`. That
example doesn't store the user roles in the document fields, as is
done in the following example.

For the budget scenario in this section, perform the following steps to create the roles, users, and `budget` collection:
