---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.1-reconfig-CWWC-validation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.1, you must set the `Cluster Wide Write Concern (CWWC) <set_global_default_write_concern>` prior to issuing any :method:`reconfigs <rs.reconfig()>` that would otherwise change the `default write concern <write-concern>` of the new `replica set` member.
