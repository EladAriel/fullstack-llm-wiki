---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-let-variable-access-note.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To reference variables in `pipeline <lookup-subquery-pipeline>` stages, use the `"$$<variable>"` syntax.

The `let <lookup-subquery-let>` variables can be accessed by the stages in the `pipeline <lookup-subquery-pipeline>`, including additional :pipeline:`$lookup` stages nested in the `pipeline`.

- A :pipeline:`$match` stage requires the use of an
:query:`$expr` operator to access the variables. The :query:`$expr` operator allows the use of aggregation expressions inside of the :pipeline:`$match` syntax.

.. include:: /includes/expr-operators-and-indexes.rst

- Other (non-:pipeline:`$match`) stages in the `pipeline <lookup-subquery-pipeline>`
do not require an :query:`$expr` operator to access the variables.
