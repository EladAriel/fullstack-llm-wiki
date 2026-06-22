---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/equality-sort-range-guideline.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# The ESR (Equality, Sort, Range) Guideline

A `compound index <index-type-compound>` references multiple fields and can dramatically improve query response times.

In most cases, applying the ESR (Equality, Sort, Range) Guideline to arrange the index keys creates a more efficient `compound index <index-type-compound>`.

Ensure that equality fields always come first. Placing equality fields first keeps the remaining index fields in sorted order. Choose whether to use a sort or range field next based on your index's specific needs:

- If avoiding in-memory sorts is critical, place sort fields before range fields
(ESR)

- If your range predicate in the query is very selective, then put it before
sort fields (ERS)

For more information on optimizing queries, see :dbcommand:`explain` and `query-plans-query-optimization`.

> **Tip:** To force MongoDB to use a particular index, use `cursor-hint`
when testing indexes.

## Equality

.. include:: /includes/sample-data-usage.rst

"Equality" refers to an exact match on a single value. The following exact match queries scan the `movies` collection for documents whose `title` field exactly matches `Equilibrium`.

Index searches make efficient use of exact matches to reduce the number of index keys examined. Equality fields must come first.

An index can have multiple equality keys. They can appear in any order relative to each other, but all equality keys must precede any sort or range fields.

The more selective the equality matches, the more efficient the indexed query.

## Sort

"Sort" determines the order for results. To avoid in-memory sorts, put sort fields before range in the index.

An index supports sort operations on a subset of its keys only when the query includes equality conditions on all prefix keys that precede the sort keys. For more information, see `Sort and Non-prefix Subset of an Index <sort-index-nonprefix-subset>`.

The following example queries the `movies` collection for movies where the `directors` field contains `"David Lynch"`. The output is sorted by `year`:

To improve query performance, create an index on the `directors` and `year` fields:

- `directors` is the first key because it is an equality match.
- `year` is indexed in the same order ( `1` ) as the query.
## Range

"Range" filters scan fields. The scan doesn't require an exact match, which means range filters are loosely bound to index keys. To improve query efficiency, limit the range bounds and use equality matches to reduce the number of documents to scan.

Range filters resemble the following:

If the range predicate in your query is very selective, place it before the sort fields to reduce the number of sorted documents and allow an in-memory sort.

To avoid an in-memory sort, place the range filter after the sort predicate. For more information on in-memory sorts, see :method:`cursor.allowDiskUse()`.

## Additional Considerations

- Inequality operators such as :query:`$ne` or :query:`$nin` are range
operators, not equality operators.

- :query:`$regex` is a range operator.
- :query:`$in`:
- When `$in` is used alone, it is an equality operator that performs a
series of equality matches.

- When `$in` is used with `.sort()`:
- If `$in` has fewer than 201 array elements, the elements are
expanded and then merged in the sort order specified for the index using a `SORT_MERGE` stage. This improves performance for small arrays. In this case, `$in` is similar to an equality predicate with ESR.

- If `$in` has 201 elements or more, the elements are ordered like
a range operator. In this case, the performance improvement for small arrays isn't realized. It isn't possible for the subsequent fields in the index to be used for sorting, and `$in` is similar to a range predicate with ESR.

- If you typically use `$in` operators with small arrays, include
them earlier in the index specification. If you typically use large arrays, include `$in` operators where you would include a range predicate.

> **Note:** The `$in` behavior change at 201 array elements is not
guaranteed to stay the same for all MongoDB versions.

## Example

The following query searches the `movies` collection for movies where the `directors` field is `"David Lynch"` and the `runtime` field is less than `130` minutes. The results are sorted by `year`:

The query contains all the elements of the ESR Guideline:

- `directors: "David Lynch"` is an equality-based match
- `runtime: { $lt: 130 }` is a range-based match
- `year` is used for sorting
Following the ESR guideline, the optimal index for the example query is:

```javascript
{ directors: 1, year: 1, runtime: 1 }
```

## Learn More

- `create-indexes-to-support-queries`
- `index-sort`
- `index-selectivity`
