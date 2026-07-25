---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-mapreduce-deprecated-bson.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:dbcommand:`mapReduce` no longer supports the deprecated `BSON Type <bson-types>` JavaScript code with scope (BSON Type 15) for its functions. The `map`, `reduce`, and `finalize` functions must be either BSON type String (BSON Type 2) or BSON Type JavaScript (BSON Type 13). To pass constant values which will be accessible in the `map`, `reduce`, and `finalize` functions, use the `scope` parameter.

The use of JavaScript code with scope for the :dbcommand:`mapReduce` functions has been deprecated since version 4.2.1.
