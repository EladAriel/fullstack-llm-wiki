---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/indexes/wildcard-use-wc-methods.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
