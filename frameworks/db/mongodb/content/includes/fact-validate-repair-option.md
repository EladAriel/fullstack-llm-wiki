---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-repair-option.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
