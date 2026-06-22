---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-fixmultikey.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. If `true`, MongoDB fixes the following issues:

- If the `validate` command finds `multikey <index-type-multikey>`
documents for a non-multikey index, MongoDB changes the index to a multikey index.

- If the `validate` command finds `multikey <index-type-multikey>`
documents that aren't specified by an index's multikey paths, MongoDB updates index's multikey paths.

The default is `false`.

.. versionadded:: 8.1
