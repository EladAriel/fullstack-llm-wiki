---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deprecation-aggregate-wo-cursor.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You must use the :dbcommand:`aggregate` command with the `cursor` option unless the command includes the `explain` option.

- To indicate a cursor with the default batch size, specify ``cursor:
{}``.

- To indicate a cursor with a non-default batch size, use ``cursor: {
batchSize: <num> }``.
