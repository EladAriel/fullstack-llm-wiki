---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/featureCompatibility-caveat.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Enabling these backwards-incompatible features can complicate the downgrade process since you must remove any persisted backwards-incompatible features before you downgrade.

It is recommended that after upgrading, you allow your deployment to run without enabling these features for a burn-in period to ensure the likelihood of downgrade is minimal. When you are confident that the likelihood of downgrade is minimal, enable these features.
