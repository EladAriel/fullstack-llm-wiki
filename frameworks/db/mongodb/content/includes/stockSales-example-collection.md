---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/stockSales-example-collection.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Create a `stockSales` collection that contains company stock financial market sales:

.. include:: /includes/stockSales-example-collection-create.rst

In the `timestamp <document-bson-type-timestamp>` constructor, the:

- First value is the number of seconds after the :wikipedia:`Unix epoch
<Unix_time>`.

- Second value is the incrementing ordinal. When multiple events happen
within the same second, the incrementing ordinal uniquely identifies each event.
