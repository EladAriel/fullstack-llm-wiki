---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/ne.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $ne (query predicate operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The `$ne` operator has the following form:

```javascript
{ field: { $ne: value } }
```

> **Note:** If the value of `$ne` is null, see `non-equality-filter`.

## Examples

.. include:: /includes/sample-data-usage.rst

### Match Document Fields That Are Not Equal

The following example returns movies where `runtime` is greater than `1000` minutes and `rated` is not equal to `"G"`. Because `$ne` also matches documents that don't contain the `rated` field, the query returns movies even when the rating data is unavailable:

### Update Based on Not Equal Embedded Document Fields

The following example sets the `highestRated` field based on a `$ne` comparison on a field in an embedded document. The :method:`~db.collection.updateMany()` operation searches for an embedded document, `imdb`, with a subfield named `rating`. It uses :update:`$set` to update the `highestRated` field to `false` in each document where the value of `rating` is not equal to `9.3` or where the `rating` subfield does not exist:

The SQL equivalent to this query is:

```sql
UPDATE movies SET highestRated = false WHERE imdb_rating != 9.3
```

.. include:: /includes/extracts/ne_operators_selectivity.rst

### Arrays

When comparing arrays, `$ne` behaves differently depending on whether you pass a scalar or an array as the comparison value.

- **Scalar comparison**: `$ne` matches documents where the
scalar value is not present as an element in the array, including documents that don't have the field.

- **Exact array comparison**: `$ne` matches documents where the
field array is not identical to the specified array, including documents with a different element order, a different number of elements, or a missing field.

The following examples return movies with a runtime over 1000 minutes to demonstrate each behavior.

Use a Scalar Comparison ```````````````````````

The following example returns movies where `runtime` is greater than `1000` minutes and `"Drama"` is not an element of the `genres` array:

Use an Exact Array Comparison `````````````````````````````

The following example returns movies where `runtime` is greater than `1000` minutes and the `genres` array is not exactly equal to `[ "Drama" ]`. Unlike the scalar comparison, `Centennial` (with `genres: [ "Action", "Adventure", "Drama" ]`) matches because that array is not identical to `[ "Drama" ]`:

## Learn More

- `sql-to-mongodb-mapping`
- `read-operations-query-document`
