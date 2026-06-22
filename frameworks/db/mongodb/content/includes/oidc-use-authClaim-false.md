---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/oidc-use-authClaim-false.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you set `useAuthorizationClaim` to `false`, users who authenticate with the `MONGODB-OIDC` mechanism obtain their authorization rights from a user document in `$external. The server searches for a user document with an id` matching the value of the `authNamePrefix/principalName` claim for every OIDC based authentication attempt for a user of your |idp|.
