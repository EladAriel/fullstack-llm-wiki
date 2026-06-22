---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-multikey/multikey-index-bounds.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# Multikey Index Bounds

**Index bounds** define the range of index values that MongoDB searches when using an index to fulfill a query. When you specify multiple query predicates on an indexed field, MongoDB attempts to combine the bounds for those predicates to produce an index scan with smaller bounds. Smaller index bounds result in faster queries and reduced resource use.

MongoDB combines bounds by either `intersecting <multikey-index-bounds-intersecting>` or `compounding <multikey-index-bounds-compound>` bounds.

## Bounds Intersection for a Multikey Index

Bounds intersection refers to the point where multiple bounds overlap. For example, given the bounds `[ [ 3, Infinity ] ]` and `[ [ -Infinity, 6 ] ]`, the intersection of the bounds results in `[ [ 3, 6 ] ]`.

Given an indexed array field, consider a query that specifies multiple query predicates on the array and uses a `multikey index <index-type-multikey>` to fulfill the query. MongoDB can intersect the multikey index bounds if an :query:`$elemMatch` operator joins the query predicates.

### Example: Bounds Intersection

The following example shows how MongoDB uses bounds intersection to define a smaller range of values to query, resulting in improved query performance.

### Query without $elemMatch

If the query does not join the conditions on the array field with `$elemMatch`, MongoDB cannot intersect the multikey index bounds.

Consider this query:

```javascript
db.students.find( { grades: { $gte: 90, $lte: 99 } } )
```

The query searches the `grades` array for:

- At least one element greater than or equal to `90`
- At least one element less than or equal to `99`
The same element can satisfy both criteria.

Because the preceding query does not use `$elemMatch`, MongoDB does not intersect the bounds. Instead, MongoDB uses either of the following bounds:

- `[ [ 90, Infinity ] ]`
- `[ [ -Infinity, 99 ] ]`
MongoDB makes no guarantee as to which of the two bounds it chooses.

## Compound Bounds for a Multikey Index

Compound bounds combine bounds for multiple keys of a `compound index <index-type-compound>`. Using bounds from multiple keys reduces the time it takes to process a query because MongoDB does not need to compute results for each bound individually.

For example, consider a compound index `{ temperature: 1, humidity: 1 }` with the following bounds:

- `temperature` has a bound of `[ [ 80, Infinity ] ]`.
- `humidity` has a bound of `[ [ -Infinity, 20 ] ]`.
Compounding the bounds results in the use of both bounds:

```javascript
{ temperature: [ [ 80, Infinity ] ], humidity: [ [ -Infinity, 20 ] ] }
```

If MongoDB cannot compound the two bounds, MongoDB constrains the index scan by the bound on the leading field. In this example, the leading field is `temperature`, resulting in a constraint of `temperature: [ [ 80, Infinity ] ]`.

### Example: Compound Bounds of Non-array Field and Array Field

The following example shows how MongoDB uses compound bounds to define a more efficient query constraint, resulting in improved query performance.

### Example: Compound Bounds of Non-array Field and Multiple Array Fields

The following example shows how MongoDB uses compound bounds when an index includes a non-array field and multiple array fields.

### Compound Bounds of Multiple Fields from the Same Array

To compound the bounds for index keys from the same array, both of the following must be true:

- The index keys must share the same field path up to but excluding the
field names.

- The query must specify predicates on the fields using
`$elemMatch` on that path.

For a field in an embedded document, the `dotted field name <document-dot-notation>`, such as `"a.b.c.d"`, is the field path for `d`. To compound the bounds for index keys from the same array, the `$elemMatch` must be on the path up to but excluding the field name itself (meaning `"a.b.c"`).

Example ```````

The following example shows how MongoDB combines bounds for index keys from the same array. This example uses the `survey2` collection used in the `previous example <index-bounds-example-non-array-multiple-array>`.

### Example: $elemMatch on Diverging Field Paths

If your query specifies `$elemMatch` on fields that diverge from a common path, MongoDB **cannot** compound the bounds of index keys from the same array.

The following example demonstrates `$elemMatch` on diverging field paths.
