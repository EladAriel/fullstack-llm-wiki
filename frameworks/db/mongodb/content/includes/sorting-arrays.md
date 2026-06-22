---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/sorting-arrays.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In array comparisons:

- An ascending sort compares the smallest
elements of the array according to the BSON type sort order.

- A descending sort compares the largest elements of the array according
to the reverse BSON type sort order.

- `query-selectors-comparison`, such as :query:`$lt` and :query:`$gt`,
perform comparisons on arrays lexicographically.

- When comparing a field whose value is a one element array (for example,
`[ 1 ]`) with non-array fields (for example, `2`), the comparison is for `1` and `2`.

- A comparison of an empty array (for example, `[ ]`) considers the empty
array as less than a `null` value or a missing field value.

- A comparison of a nested array (for example, `[[1, 2], [3, 4]]`) compares
any array after the outmost array lexicographically.
