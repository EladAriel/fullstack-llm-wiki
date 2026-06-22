---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.skip.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# cursor.skip() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Using `skip()` with `sort()`

If using :method:`~cursor.skip()` with :method:`~cursor.sort()`, be sure to include at least one field in your sort that contains unique values, before passing results to :method:`~cursor.skip()`.

Sorting on fields that contain duplicate values may return an inconsistent sort order for those duplicate fields over multiple executions, especially when the collection is actively receiving writes.

The easiest way to guarantee sort consistency is to include the `_id` field in your sort query.

See `Consistent sorting with the sort() method <sort-cursor-consistent-sorting>` for more information.

### Using `skip()` with `limit()`

.. include:: includes/reference/skip-limit.rst

## Pagination Example

### Using `skip()`

The following JavaScript function uses :method:`~cursor.skip() to paginate a collection by its id` field:

```javascript
function printStudents(pageNumber, nPerPage) {
  print( "Page: " + pageNumber );
  db.students.find()
             .sort( { _id: 1 } )
             .skip( pageNumber > 0 ? ( ( pageNumber - 1 ) * nPerPage ) : 0 )
             .limit( nPerPage )
             .forEach( student => {
               print( student.name );
             } );
}
```

The :method:`~cursor.skip()` method requires the server to scan from the beginning of the input results set before beginning to return results. As the offset increases, :method:`~cursor.skip()` will become slower.

### Using Range Queries

Range queries can use `indexes <indexes>` to avoid scanning unwanted documents, typically yielding better performance as the offset grows compared to using :method:`~cursor.skip()` for pagination.

Descending Order ````````````````

Use this procedure to implement pagination with range queries:

- Choose a field such as `_id` which generally changes in a consistent
direction over time and has a `unique index <index-type-unique>` to prevent duplicate values,

- Query for documents whose field is less than the start value
using the :query:`$lt` and :method:`~cursor.sort()` operators, and

- Store the last-seen field value for the next query.
For example, the following function uses the above procedure to print pages of student names from a collection, sorted approximately in order of newest documents first using the `_id` field (that is, in descending order):

```javascript
function printStudents(startValue, nPerPage) {
  let endValue = null;
  db.students.find( { _id: { $lt: startValue } } )
             .sort( { _id: -1 } )
             .limit( nPerPage )
             .forEach( student => {
               print( student.name );
               endValue = student._id;
             } );

  return endValue;
}
```

You may then use the following code to print all student names using this pagination function, using :bsontype:`MaxKey` to start from the largest possible key:

```javascript
let currentKey = MaxKey;
while (currentKey !== null) {
  currentKey = printStudents(currentKey, 10);
}
```

> **Note:** .. include:: /includes/fact-ObjectId-timestamp-order.rst

Ascending Order ```````````````

Returning paginated results in ascending order is similar to the previous, but uses :query:`$gt` with an ascending sort order:

```javascript
function printStudents(startValue, nPerPage) {
  let endValue = null;
  db.students.find( { _id: { $gt: startValue } } )
             .sort( { _id: 1 } )
             .limit( nPerPage )
             .forEach( student => {
               print( student.name );
               endValue = student._id;
             } );

  return endValue;
}
```

Using this function is likewise similar, but with :bsontype:`MinKey` as the starting key:

```javascript
let currentKey = MinKey;
while (currentKey !== null) {
  currentKey = printStudents(currentKey, 10);
}
```
