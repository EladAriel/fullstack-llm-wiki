---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-conformance.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Optional. If `true`, the collection is checked to ensure the `BSON documents <bson-document-format>` conform to the BSON specifications. The checks increase the time to complete the validation operation. Any issues are returned as a warning.

`checkBSONConformance`:

- Default is `false`.
- Cannot be used with:
- `repair` set to `true`.
- `metadata` set to `true`.
.. versionadded:: 6.2
