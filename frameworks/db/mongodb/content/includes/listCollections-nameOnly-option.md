---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/listCollections-nameOnly-option.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. A flag to indicate whether the command returns just the name and type (`view`, `collection`, or `timeseries`) or returns both the name and other information.

The default value is `false`.

When `nameOnly` is `true`, your `filter` expression can only filter based on a collection's name and type. No other fields are available.
