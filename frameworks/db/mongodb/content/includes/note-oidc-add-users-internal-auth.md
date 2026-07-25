---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-oidc-add-users-internal-auth.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** Your :parameter:`oidcIdentityProviders` configuration determines the
approach you must take to authorize users:
- If the `useAuthorizationClaim` field is set to `false` to enable
  internal authorization, authorize users with user IDs.
- If the field is set to `true`, authorize users with |idp|
  groups.
