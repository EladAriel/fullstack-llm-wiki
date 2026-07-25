---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-concurrent-read-write-dynamic-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** Starting in version 7.0, MongoDB dynamically adjusts the number of
tickets to optimize performance, with a highest possible value of 128.
Modifying this value can cause performance issues or errors. To
determine if disabling the dynamic concurrent storage engine
transactions algorithm is optimal for the cluster, contact
[MongoDB Support](https://www.mongodb.com/docs/manual/support/)_.
