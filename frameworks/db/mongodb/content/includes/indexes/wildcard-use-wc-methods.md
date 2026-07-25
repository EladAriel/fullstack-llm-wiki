---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-use-wc-methods.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB supports several different index types, including:

- `text <index-feature-text>`
- `geospatial <index-feature-geospatial>`
- `hashed indexes <index-type-hashed>`
See `index types <index-types>` for more information.

`Wildcard indexes <wildcard-index-core>` support workloads where users query against custom fields or a large variety of fields in a collection:

- You can create a wildcard index on a specific field and its
subpaths or on all of the fields in a document.

For details see, `wildcard-index-core`.
