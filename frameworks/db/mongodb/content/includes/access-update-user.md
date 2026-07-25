---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-update-user.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You must have access that includes the :authaction:`revokeRole` `action <security-user-actions>` on all databases in order to update a user's `admin.system.users.roles` array.

You must have the :authaction:`grantRole` `action <security-user-actions>` on a role's database to add a role to a user.

To change another user's `pwd` or `customData` field, you must have the :authaction:`changePassword` and :authaction:`changeCustomData` `actions <security-user-actions>` respectively on that user's database.
