---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-limitation-one-geo-index-per-collection.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You can specify a `key` option to the :pipeline:`$geoNear` pipeline stage to indicate the indexed field path to use. This allows the :pipeline:`$geoNear` stage to be used on a collection that has multiple |first-geo-index| and/or multiple |second-geo-index|:

- If your collection has multiple |first-geo-index| and/or multiple
|second-geo-index|, you must use the `key` option to specify the indexed field path to use.

- If you do not specify the `key`, you cannot have multiple
|first-geo-index| and/or multiple |second-geo-index| since without the `key`, index selection among multiple `2d` indexes or `2dsphere` indexes is ambiguous.

> **Note:** If you do not specify the `key`, and you have at most only one
|first-geo-index| and/or only one |second-geo-index|,
MongoDB looks first for a `2d` index to use. If a `2d` index
does not exists, then MongoDB looks for a `2dsphere` index to use.
