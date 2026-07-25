---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream/ud-disambiguatedPaths.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

A document that provides clarification of ambiguous field descriptors in `updateDescription`.

When the `update` change event describes changes on a field where the path contains a period (`.`) or where the path includes a non-array numeric subfield, the `disambiguatedPath` field provides a document with an array that lists each entry in the path to the modified field.

Requires that you set the `showExpandedEvents <change-streams-expanded-events>` option to `true`.

.. versionadded:: 6.1
