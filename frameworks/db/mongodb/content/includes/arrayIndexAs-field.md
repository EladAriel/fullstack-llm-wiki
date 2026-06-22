---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/arrayIndexAs-field.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. A name for the `aggregation variable <aggregation-variables>` that represents the index of the current element in the `input` array. The first array element index is `0`.

You can use the variable name in an expression. For example, if you specify `arrayIndexAs: "myIndex"`, you use `$$myIndex` in the expression. `$$myIndex` returns the index of the current element in the `input` array.

If you omit `arrayIndexAs`, you can use the :variable:`$$IDX <IDX>` system variable in the expression to return the index of the current element.
