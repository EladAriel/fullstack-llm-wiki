---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-standalone-inconsistencies.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Index inconsistencies include:

- An index is `multikey <index-type-multikey>` but there are
no multikey fields.

- An index has `multikeyPaths <compound_multikey_indexes>` covering
fields that are not multikey.

- An index does not have
`multikeyPaths <compound_multikey_indexes>` but there are multikey documents (for indexes built before 3.4).

If any inconsistencies are detected by the :method:`db.collection.validate()` command, a warning is returned and the repair flag on the index is set to `true`.

:method:`db.collection.validate()` also validates any documents that violate the collection's `schema validation rules <schema-validation-document>`.
