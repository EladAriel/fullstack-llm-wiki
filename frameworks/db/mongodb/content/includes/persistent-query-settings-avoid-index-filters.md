---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/persistent-query-settings-avoid-index-filters.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

.. versionadded:: 8.0

.. include:: /includes/persistent-query-settings-avoid-index-filters-intro.rst

The `query optimizer` uses the query settings as an additional input during query planning, which affects the plan selected to run the query.

The settings apply to the `query shape <queryStats-queryShape>` on the entire cluster. The cluster retains the settings after shutdown.

You can add query settings for :dbcommand:`find`, :dbcommand:`distinct`, and :dbcommand:`aggregate` commands.

To remove query settings, use :dbcommand:`removeQuerySettings`. To obtain the query settings, use a :pipeline:`$querySettings` stage in an aggregation pipeline.
