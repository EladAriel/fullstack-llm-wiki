---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/valid-ttl-config-prereq.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Ensure TTL Config is Valid

Ensure that the `TTL <ttl-collections>` configuration is valid. Before upgrading, remove or correct any TTL indexes that have `expireAfterSeconds` set to `NaN`. In MongoDB 5.0 and later, setting `expireAfterSeconds` to `NaN` has the same effect as setting `expireAfterSeconds` to `0`. For details, see `<ttl_expireAfterSeconds_behavior>`.
