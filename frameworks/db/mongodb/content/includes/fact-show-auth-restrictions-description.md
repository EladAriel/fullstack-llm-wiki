---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-show-auth-restrictions-description.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. Set this field to `true` to include `authentication restrictions <create-role-auth-restrictions>` in the output. Authentication restrictions indicate the IP addresses that users with this role can connect to and from.

By default, this field is `false`, meaning that the |getRoleMethod| output does not include authentication restrictions.
