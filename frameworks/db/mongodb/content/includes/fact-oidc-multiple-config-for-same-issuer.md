---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-oidc-multiple-config-for-same-issuer.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.0, when multiple |idps| are defined, the :parameter:`oidcIdentityProviders` parameter accepts duplicate `issuer` values as long as the `audience` value is unique for each issuer. This is also available in versions 7.3 and 7.0.
