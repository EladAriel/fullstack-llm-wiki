---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-update-example-middle.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The previous example uses :expression:`$setIntersection` to return documents where the intersection between the `"Provider"` string and the user roles from `$$USER_ROLES.role` is not empty. `Michelle` has the `Provider` role, so the update is performed.

Next, log in as as `James`, who does not have the `Provider` role, and attempt to perform the same update:
