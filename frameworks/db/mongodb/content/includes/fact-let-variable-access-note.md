---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-let-variable-access-note.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To reference variables in `pipeline <lookup-subquery-pipeline>` stages, use the `"$$<variable>"` syntax.

The `let <lookup-subquery-let>` variables can be accessed by the stages in the `pipeline <lookup-subquery-pipeline>`, including additional :pipeline:`$lookup` stages nested in the `pipeline`.

- A :pipeline:`$match` stage requires the use of an
:query:`$expr` operator to access the variables. The :query:`$expr` operator allows the use of aggregation expressions inside of the :pipeline:`$match` syntax.

.. include:: /includes/expr-operators-and-indexes.rst

- Other (non-:pipeline:`$match`) stages in the `pipeline <lookup-subquery-pipeline>`
do not require an :query:`$expr` operator to access the variables.
