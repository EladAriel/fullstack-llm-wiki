---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/collation-index-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Use the following code to create an index on the `movies` collection of the `sample_mflix` database with the collation locale `"fr"` for string comparisons:

The following query, which specifies the same collation as the index, can use the index:

However, the following query operation, which by default uses the "simple" binary collator, cannot use the index and requires a `COLLSCAN`.

For a compound index where the index prefix keys are not strings, arrays, and embedded documents, an operation that specifies a different collation can still use the index to support comparisons on the index prefix keys.

For example, you can use the following code to create a compound index on the `movies` collection of the `sample_mflix` database specifying the numeric fields `year` and `metacritic` and the string field `title`. The index also specifies the collation locale `"fr"` for string comparisons:

The following operations, which use `"simple"` binary collation for string comparisons, can use the index:

The following operation, which uses `"simple"` binary collation for string comparisons on the indexed `title` field, can use the index to fulfill only the `year: 2012` portion of the query:

To confirm whether a query used an index, run the query with the :method:`~cursor.explain()` option.

> **Important:** Matches against document keys, including embedded document keys,
use simple binary comparison. This means that a query for a key
like "type.café" will not match the key "type.cafe", regardless of
the value you set for the :ref:`strength
<collation-parameter-strength>` parameter.
