---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-schema-validation.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you have `{+csfle+} <manual-csfle-feature>` or `{+qe+} <qe-manual-feature-qe>` enabled on a collection, validation is subject to the following restrictions:

- For {+csfle-abbrev+}, when running :dbcommand:`collMod`, the
`libmongocrypt<qe-reference-libmongocrypt>` library prefers the JSON `{+enc-schema+} <csfle-fundamentals-create-schema>` specified in the command. This preference enables setting a schema on a collection that does not yet have one.

- For {+qe+}, any JSON schema that includes an encrypted field results in a
query analysis error.
