---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-single.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Single Field Indexes

Single field indexes store information from a single field in a collection. By default, all collections have an index on the `_id field <index-type-id>`. You can add additional indexes to speed up important queries and operations.

You can create an index on any field in a document, including top-level fields, embedded fields, or fields inside embedded documents. When you create an index, specify the field and the sort order (`1` for ascending, `-1` for descending).

To create a single-field index, use the following prototype:

.. include:: /includes/indexes/code-examples/create-single-field-index.rst

This image shows an ascending index on a single field, `score`:

.. include:: /images/index-ascending.rst

In this example, each document in the collection that has a value for the `score` field is added to the index in ascending order.

## Use Cases

If your application repeatedly runs queries on the same field, you can create an index on that field to improve performance. For example, your human resources department often needs to look up employees by employee ID. You can create an index on the employee ID field to improve the performance of that query.

## Get Started

To create an index on a single field, see these examples:

- `index-create-ascending-single-field`
- `index-embedded-fields`
- `index-embedded-documents`
## Contents

- Create </core/indexes/index-types/index-single/create-single-field-index>
- Embedded Documents </core/indexes/index-types/index-single/create-embedded-object-index>
