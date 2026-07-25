---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-update-example-middle.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The previous example uses :expression:`$setIntersection` to return documents where the intersection between the `"Provider"` string and the user roles from `$$USER_ROLES.role` is not empty. `Michelle` has the `Provider` role, so the update is performed.

Next, log in as as `James`, who does not have the `Provider` role, and attempt to perform the same update:
