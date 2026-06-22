---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-update-user.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You must have access that includes the :authaction:`revokeRole` `action <security-user-actions>` on all databases in order to update a user's `admin.system.users.roles` array.

You must have the :authaction:`grantRole` `action <security-user-actions>` on a role's database to add a role to a user.

To change another user's `pwd` or `customData` field, you must have the :authaction:`changePassword` and :authaction:`changeCustomData` `actions <security-user-actions>` respectively on that user's database.
