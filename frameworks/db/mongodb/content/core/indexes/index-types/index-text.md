---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# Text Indexes on Self-Managed Deployments

.. include:: /includes/fact-fts-avs-text-index.rst

Text indexes support :query:`$text` `queries <text-query>` on fields that contain string content. They also support `aggregation expressions <qe-aggregation-operators>` for encrypted string fields in `{+qe+} <qe-manual-feature-qe>` enabled collections. Text indexes improve performance when you search for specific words or strings within string content.

A collection can have only **one** text index, but that index may include multiple fields.

To create a text index, use the following prototype:

.. include:: /includes/indexes/code-examples/create-text-index.rst

## Support for the $text Operator

Text indexes support :query:`$text` query operations on on-premises deployments. To use `$text`, you must create a text index.

## $encStr Support

Text indexes support `aggregation expressions <qe-aggregation-operators>` for fields in {+qe+} collections with prefix, suffix, or substring queries enabled. A text index is required to use the :expression:`$encStrNormalizedEq` expression.

## Use Cases

An online shop's `clothing` collection has a `description` field that contains a string of text describing each item. To find clothes made of `"silk"`, create a text index on `description` and run a `$text` query for `"silk"`. The search returns all documents mentioning `"silk"` in `description`.

## Get Started

To learn how to create and use text indexes, see:

- `<create-text-index>`
- `<create-wildcard-text-index>`
- `<specify-default-text-index-language>`
- `limit-entries-scanned`
## Details

This section describes text index details.

### Compound Text Indexes

In a compound index with a text index key and other key types, only the text index field determines whether the index references a document. Other keys do not affect document references.

### Covered Queries

.. include:: /includes/fact-text-index-covered-query.rst

### `sparse` Property

Text indexes are always `sparse <index-type-sparse>`. MongoDB ignores the `sparse` option when creating text indexes.

MongoDB does not add a text index entry for documents that lack the text index field, have null values, or have empty arrays.

### Storage Requirements and Performance Costs

Text indexes have these storage and performance characteristics:

- Text indexes can consume significant RAM. They contain one
index entry for each unique stemmed word in each indexed field for each document.

- Building a text index is similar to building a large
`multikey index <index-type-multi-key>` but takes longer than building an ordered (scalar) index on the same data.

- When building large text indexes, ensure sufficient file
descriptor limits. See `recommended settings <ulimit>`.

- Text indexes impact write performance because MongoDB must add
an index entry for each unique stemmed word in each indexed field of new documents.

- Text indexes store individual words, not multi-word strings or
word proximity information. Queries with multiple words run faster when the entire collection fits in RAM.

## Learn More

- To learn more about text indexes, see:
- `<control-text-search-results>`
- `<text-index-properties>`
- `<text-index-restrictions>`
- `<text-index-versions>`
- For `$text` query examples, see the :query:`$text reference page <$text>`.
- For sample `$text` operations in aggregation pipelines, see
`<text-agg>`.

## Contents

- Create </core/indexes/index-types/index-text/create-text-index>
- Create a Wildcard </core/indexes/index-types/index-text/create-wildcard-text-index>
- Specify Language </core/indexes/index-types/index-text/specify-text-index-language>
- Assign Weights </core/indexes/index-types/index-text/control-text-search-results>
- Limit Entries </core/indexes/index-types/index-text/limit-number-of-items-scanned-for-text-search>
- Properties </core/indexes/index-types/index-text/text-index-properties>
- Restrictions </core/indexes/index-types/index-text/text-index-restrictions>
- Versions </core/indexes/index-types/index-text/text-index-versions>
