---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/expression-components.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In the MongoDB Query Language, you can build expressions from the following components:

For example, `{ $add: [ 3, "$inventory.total" ] }` is an expression that consists of the `$add` operator and two operands:

- The constant `3`
- The `field path expression <agg-quick-ref-field-paths>`
`"$inventory.total"`

The expression returns the result of adding 3 to the value at path `inventory.total` of the input document.
