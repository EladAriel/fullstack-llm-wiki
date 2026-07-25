---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-show-auth-restrictions-description.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. Set this field to `true` to include `authentication restrictions <create-role-auth-restrictions>` in the output. Authentication restrictions indicate the IP addresses that users with this role can connect to and from.

By default, this field is `false`, meaning that the |getRoleMethod| output does not include authentication restrictions.
