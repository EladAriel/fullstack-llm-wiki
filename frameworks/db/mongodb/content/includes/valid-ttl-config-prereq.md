---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/valid-ttl-config-prereq.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Ensure TTL Config is Valid

Ensure that the `TTL <ttl-collections>` configuration is valid. Before upgrading, remove or correct any TTL indexes that have `expireAfterSeconds` set to `NaN`. In MongoDB 5.0 and later, setting `expireAfterSeconds` to `NaN` has the same effect as setting `expireAfterSeconds` to `0`. For details, see `<ttl_expireAfterSeconds_behavior>`.
