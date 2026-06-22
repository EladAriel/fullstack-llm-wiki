---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/persistent-query-settings-avoid-index-filters-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.0, use query settings instead of adding `index filters <index-filters>`. Index filters are deprecated starting in MongoDB 8.0.

Query settings have more functionality than index filters. Also, index filters aren't persistent and you cannot easily create index filters for all cluster nodes. To add query settings and explore examples, see :dbcommand:`setQuerySettings`.
