---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/timeseries-distinct-command-javascript.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Due to the unique data structure of time series collections, MongoDB can't efficiently index them for distinct values. Avoid using the :dbcommand:`distinct` command or :method:`db.collection.distinct()` helper method on time series collections. Instead, use a :pipeline:`$group` aggregation to group documents by distinct values, as shown in the following example:

This works as follows:

#. Creating a `compound index <index-type-compound>` on `meta.project` and `meta.type` and supports the aggregation.

#. The :pipeline:`$match` stage filters for documents where `meta.project = 10`.

#. The :pipeline:`$group` stage uses `meta.type` as the group key to output one document per unique value.
