---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/expr-operators-and-indexes.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The :expression:`$eq`, :expression:`$lt`, :expression:`$lte`, :expression:`$gt`, and :expression:`$gte` comparison operators placed in an :query:`$expr` operator can use an index on the `from` collection referenced in a :pipeline:`$lookup` stage. Limitations:

- Indexes can only be used for comparisons between fields and constants, so the
`let` operand must resolve to a constant.

For example, a comparison between `$a` and a constant value can use an index, but a comparison between `$a` and `$b` cannot.

- Indexes are not used for comparisons where the `let` operand resolves to an
empty or missing value.

- `Multikey <index-type-multikey>`, `partial <index-type-partial>`, or
`sparse <index-type-sparse>` indexes are not used.
