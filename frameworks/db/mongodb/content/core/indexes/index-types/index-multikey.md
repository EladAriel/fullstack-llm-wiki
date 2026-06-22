---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-multikey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# Multikey Indexes

Multikey indexes collect and sort data from fields containing array values. Multikey indexes improve performance for queries on array fields.

When you create an index on a field that contains an array value, MongoDB automatically sets that index to be a multikey index.

MongoDB can create multikey indexes over arrays that hold both scalar values (for example, strings and numbers) and embedded documents. If an array contains multiple instances of the same value, the index only includes one entry for the value.

To create a multikey index, use the following prototype:

.. include:: /includes/indexes/code-examples/create-multikey-index.rst

This image shows a multikey index on the `addr.zip` field:

.. include:: /images/index-multikey.rst

## Use Cases

If your application frequently queries a field that contains an array value, a multikey index improves performance for those queries.

For example, documents in a `movies` collection contain a `genres` field: an array of genres associated with each movie. You regularly query movies that have specific genres, such as finding all movies that are both `Drama` and `Action`.

You can create an index on the `genres` field to improve performance for this query. Because `genres` contains an array value, MongoDB stores the index as a multikey index.

## Get Started

To create a multikey index, see:

- `index-create-multikey-scalar`
- `index-create-multikey-embedded`
## Details

This section describes technical details and limitations for multikey indexes.

.. include:: /includes/sample-data-usage.rst

### Index Bounds

The bounds of an index scan define the parts of an index to search during a query. The computation of multikey index bounds follows special rules. For details, see `indexes-multikey-bounds`.

### Unique Multikey Indexes

In a `unique <index-type-unique>` multikey index, a document may have array elements that result in repeating index key values as long as the index key values for that document do not duplicate those of another document.

To learn more and see an example of this behavior, see `unique-separate-documents`.

### Compound Multikey Indexes

In a `compound <index-type-compound>` multikey index, each indexed document can have at most one indexed field whose value is an array. Specifically:

- You cannot create a compound multikey index if more than one field in
the index specification is an array.

- If a compound multikey index already exists, you cannot insert a
document that would violate this restriction.

For example, you can create a compound multikey index `{ genres: 1, year: 1 }` on the `movies` collection because for each document, only one field indexed by the compound multikey index is an array. No document contains array values for both `genres` and `year` fields.

However, after you create the compound multikey index, if you attempt to insert a document where both `genres` and `year` fields are arrays, the insert fails.

### Sorting

.. include:: /includes/fact-multikey-index-sort-limitation.rst

### Shard Keys

You cannot specify a multikey index as a shard key index.

However, if the shard key index is a `prefix <compound-index-prefix>` of a compound index, the compound index may become a compound multikey index if one of the trailing keys (that are not part of the shard key) indexes an array.

### Hashed Indexes

`Hashed indexes <index-type-hashed>` cannot be multikey.

### Covered Queries

Multikey indexes can cover queries when these conditions are met:

- The query does not return the array field (meaning the array is not
included in the query projection). This means that to cover a query, the multikey index must be `compound <compound_multikey_indexes>`.

- The query does not include :query:`$elemMatch`.
- The query meets all other :ref:`covered query requirements
<covered-queries>`.

For example, the following operation creates a compound multikey index on the `movies` collection on the `genres` and `title` fields:

The preceding index is multikey because the `genres` field contains array values.

The index covers these queries:

The index does not cover the following query because the projection contains the `genres` array field:

### Query on an Array Field as a Whole

When a query specifies an `exact match for an array as a whole <array-match-exact>`, MongoDB uses the multikey index to locate documents that contain the first element of that array. However, it cannot match the entire array using the index alone. MongoDB then fetches the candidate documents and filters them to return only those whose array exactly matches the query array.

For example, the following operation creates a multikey index on the `movies` collection on the `genres` field:

The following query looks for documents where the `genres` field is the array `[ "Drama" ]`:

MongoDB can use the multikey index to find documents that have `"Drama"` at any position in the `genres` array. Then, MongoDB retrieves these documents and filters for documents whose `genres` array equals the query array `[ "Drama" ]`.

### $expr

The :query:`$expr` operator does not support multikey indexes.

## Learn More

- To learn how MongoDB combines multikey index bounds to improve
performance, see `indexes-multikey-bounds`.

- To learn how to query array fields, see:
- `read-operations-arrays`
- `array-match-embedded-documents`
## Contents

- Create on Array Field </core/indexes/index-types/index-multikey/create-multikey-index-basic>
- Embedded Array Field </core/indexes/index-types/index-multikey/create-multikey-index-embedded>
- Bounds </core/indexes/index-types/index-multikey/multikey-index-bounds>
