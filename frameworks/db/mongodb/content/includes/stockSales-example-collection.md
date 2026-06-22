---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/stockSales-example-collection.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Create a `stockSales` collection that contains company stock financial market sales:

.. include:: /includes/stockSales-example-collection-create.rst

In the `timestamp <document-bson-type-timestamp>` constructor, the:

- First value is the number of seconds after the :wikipedia:`Unix epoch
<Unix_time>`.

- Second value is the incrementing ordinal. When multiple events happen
within the same second, the incrementing ordinal uniquely identifies each event.
