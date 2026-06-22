---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-update-example-introduction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 7.0, you can use the new :variable:`USER_ROLES` system variable to return user `roles <roles>`.

The example in this section shows updates to fields in a collection containing medical information. The example reads the current user roles from the `USER_ROLES` system variable and only performs the updates if the user has a specific role.

.. include:: /includes/user-roles-system-variable-example-description-start.rst

The example creates these users:

- `James` with a `Billing` role.
- `Michelle` with a `Provider` role.
Perform the following steps to create the roles, users, and collection:

Log in as as `Michelle`, who has the `Provider` role, and perform an update:
