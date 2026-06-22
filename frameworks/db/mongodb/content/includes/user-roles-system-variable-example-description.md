---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-example-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The previous example returns the documents from the `budget` collection that match at least one of the roles that the user who runs the example has. To do that, the example uses :expression:`$setIntersection` to return documents where the intersection between the `budget` document `allowedRoles` field and the set of user roles from `$$USER_ROLES` is not empty.
