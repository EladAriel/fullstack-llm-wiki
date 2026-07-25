---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deprecation-aggregate-wo-cursor.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You must use the :dbcommand:`aggregate` command with the `cursor` option unless the command includes the `explain` option.

- To indicate a cursor with the default batch size, specify ``cursor:
{}``.

- To indicate a cursor with a non-default batch size, use ``cursor: {
batchSize: <num> }``.
