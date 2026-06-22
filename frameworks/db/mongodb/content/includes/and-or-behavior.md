---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/and-or-behavior.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To allow the query engine to optimize queries, |and-or| handles errors as follows:

- If any expression supplied to |and-or| would cause an error when
evaluated alone, the |and-or| containing the expression may cause an error but an error is not guaranteed.

- An expression supplied after the first expression supplied to |and-or|
may cause an error even if the first expression evaluates to |true-false|.
