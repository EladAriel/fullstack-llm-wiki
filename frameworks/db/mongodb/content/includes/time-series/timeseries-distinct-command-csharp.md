---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/timeseries-distinct-command-csharp.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Due to the unique data structure of time series collections, MongoDB can't efficiently index them for distinct values. Avoid using the :dbcommand:`distinct` command or :method:`db.collection.distinct()` helper method on time series collections. Instead, use a :pipeline:`$group` aggregation to group documents by distinct values, as shown in the following example:

This works as follows:

#. Creating a `compound index <index-type-compound>` on `meta.project` and `meta.type` and supports the aggregation.

#. The :pipeline:`$match` stage filters for documents where `meta.project = 10`.

#. The :pipeline:`$group` stage uses `meta.type` as the group key to output one document per unique value.
