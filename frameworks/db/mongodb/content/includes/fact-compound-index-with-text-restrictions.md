---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-compound-index-with-text-restrictions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- A compound text index cannot include any other special index types,
such as `multikey <index-type-multi-key>` or `geospatial <geospatial-index>` index fields.

- If the compound text index includes keys **preceding** the text index
key, to use :query:`$text`, the query predicate must include **equality match conditions** on the preceding keys.

- When you create a compound text index, all text index keys must be
listed adjacently in the index specification document.
