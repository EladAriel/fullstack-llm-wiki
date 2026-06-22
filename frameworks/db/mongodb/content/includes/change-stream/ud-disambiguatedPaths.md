---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/ud-disambiguatedPaths.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A document that provides clarification of ambiguous field descriptors in `updateDescription`.

When the `update` change event describes changes on a field where the path contains a period (`.`) or where the path includes a non-array numeric subfield, the `disambiguatedPath` field provides a document with an array that lists each entry in the path to the modified field.

Requires that you set the `showExpandedEvents <change-streams-expanded-events>` option to `true`.

.. versionadded:: 6.1
