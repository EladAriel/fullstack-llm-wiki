---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/data-modeling/duplicate-data-considerations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Before you duplicate data, consider the following factors:

- The performance benefit for reads when data is duplicated. Duplicating
data can remove the need to perform joins across multiple collections, which can improve application performance.

- How often the duplicated data needs to be updated. The extra logic needed to
handle infrequent updates is less costly than performing joins (lookups) on read operations. However, frequently updating duplicate data can cause heavy workloads and performance issues.
