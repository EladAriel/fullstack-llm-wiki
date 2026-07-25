---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-eMRC-always-true-in-5.0.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, :setting:`~replication.enableMajorityReadConcern` and :option:`--enableMajorityReadConcern` cannot be changed and are always set to `true` due to storage engine improvements.

In earlier versions of MongoDB, :setting:`~replication.enableMajorityReadConcern` and :option:`--enableMajorityReadConcern` are configurable and can be set to `false` to prevent storage cache pressure from immobilizing a deployment with a three-member primary-secondary-arbiter (PSA) architecture.
