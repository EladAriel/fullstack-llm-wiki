---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-repair-option.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. A flag that determines whether the command performs a repair.

- If `true`, a repair is performed.
- If `false`, no repair is performed.
The default is `false`.

A repair can only be run on a standalone node.

The repair fixes the following issues:

- If missing index entries are found, the missing keys are inserted into
the index.

- If extra index entries are found, the extra keys are removed from the
index.

- If corrupt documents with invalid BSON data are found, the documents
are removed.

:gold:`IMPORTANT:` To set `repair` to `true`, you must set the `fixMultikey` option to `true`.

For more information, see the :option:`--repair <mongod --repair>` option for :binary:`~bin.mongod`

.. versionadded:: 5.0
