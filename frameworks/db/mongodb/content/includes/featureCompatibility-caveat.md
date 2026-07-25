---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/featureCompatibility-caveat.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Enabling these backwards-incompatible features can complicate the downgrade process since you must remove any persisted backwards-incompatible features before you downgrade.

It is recommended that after upgrading, you allow your deployment to run without enabling these features for a burn-in period to ensure the likelihood of downgrade is minimal. When you are confident that the likelihood of downgrade is minimal, enable these features.
