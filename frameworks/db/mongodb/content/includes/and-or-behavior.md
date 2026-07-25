---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/and-or-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To allow the query engine to optimize queries, |and-or| handles errors as follows:

- If any expression supplied to |and-or| would cause an error when
evaluated alone, the |and-or| containing the expression may cause an error but an error is not guaranteed.

- An expression supplied after the first expression supplied to |and-or|
may cause an error even if the first expression evaluates to |true-false|.
