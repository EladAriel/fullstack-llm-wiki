---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-fixmultikey.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. If `true`, MongoDB fixes the following issues:

- If the `validate` command finds `multikey <index-type-multikey>`
documents for a non-multikey index, MongoDB changes the index to a multikey index.

- If the `validate` command finds `multikey <index-type-multikey>`
documents that aren't specified by an index's multikey paths, MongoDB updates index's multikey paths.

The default is `false`.

.. versionadded:: 8.1
