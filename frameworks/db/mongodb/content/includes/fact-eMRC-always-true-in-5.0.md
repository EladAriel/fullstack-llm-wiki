---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-eMRC-always-true-in-5.0.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, :setting:`~replication.enableMajorityReadConcern` and :option:`--enableMajorityReadConcern` cannot be changed and are always set to `true` due to storage engine improvements.

In earlier versions of MongoDB, :setting:`~replication.enableMajorityReadConcern` and :option:`--enableMajorityReadConcern` are configurable and can be set to `false` to prevent storage cache pressure from immobilizing a deployment with a three-member primary-secondary-arbiter (PSA) architecture.
