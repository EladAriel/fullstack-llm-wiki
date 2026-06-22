---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-conformance.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. If `true`, the collection is checked to ensure the `BSON documents <bson-document-format>` conform to the BSON specifications. The checks increase the time to complete the validation operation. Any issues are returned as a warning.

`checkBSONConformance`:

- Default is `false`.
- Cannot be used with:
- `repair` set to `true`.
- `metadata` set to `true`.
.. versionadded:: 6.2
