---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/agg-expression-order-of-return-behavior.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When input types are mixed, |operatorName| promotes the smaller input type to the larger of the two. A type is considered larger when it represents a wider range of values. The order of numeric types from smallest to largest is: integer → long → double → decimal

The larger of the input types also determines the result type unless the operation overflows and is beyond the range represented by that larger data type. In cases of overflow, |operatorName| promotes the result according to the following order:

- If the larger input type is :bsontype:`integer <Int32>`, the result type
is promoted to :bsontype:`long <Int64>`.

- If the larger input type is :bsontype:`long <Int64>`, the result type is
promoted to :bsontype:`double <Double>`.

- If the larger type is :bsontype:`double <Double>` or
:bsontype:`decimal <Decimal128>`, the overflow result is represented as + or - infinity. There is no type promotion of the result.
