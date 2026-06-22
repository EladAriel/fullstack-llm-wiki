---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-concurrent-read-write-dynamic-behavior.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** Starting in version 7.0, MongoDB dynamically adjusts the number of
tickets to optimize performance, with a highest possible value of 128.
Modifying this value can cause performance issues or errors. To
determine if disabling the dynamic concurrent storage engine
transactions algorithm is optimal for the cluster, contact
[MongoDB Support](https://www.mongodb.com/docs/manual/support/)_.
