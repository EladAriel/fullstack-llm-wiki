---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-mapreduce-deprecated-bson.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:dbcommand:`mapReduce` no longer supports the deprecated `BSON Type <bson-types>` JavaScript code with scope (BSON Type 15) for its functions. The `map`, `reduce`, and `finalize` functions must be either BSON type String (BSON Type 2) or BSON Type JavaScript (BSON Type 13). To pass constant values which will be accessible in the `map`, `reduce`, and `finalize` functions, use the `scope` parameter.

The use of JavaScript code with scope for the :dbcommand:`mapReduce` functions has been deprecated since version 4.2.1.
