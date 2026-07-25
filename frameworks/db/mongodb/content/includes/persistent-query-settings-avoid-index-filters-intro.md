---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/persistent-query-settings-avoid-index-filters-intro.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.0, use query settings instead of adding `index filters <index-filters>`. Index filters are deprecated starting in MongoDB 8.0.

Query settings have more functionality than index filters. Also, index filters aren't persistent and you cannot easily create index filters for all cluster nodes. To add query settings and explore examples, see :dbcommand:`setQuerySettings`.
