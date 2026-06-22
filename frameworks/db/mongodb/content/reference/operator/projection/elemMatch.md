---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/projection/elemMatch.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $elemMatch (projection operator)

> **Seealso:** `/reference/operator/query/elemMatch`

## Definition

## Usage Considerations

### Returned Element

.. include:: /includes/fact-positional-projection-vs-elemmatch.rst

### Field Order

.. include:: /includes/extracts/projection-elemMatch-projection-field-order.rst

### Restrictions

- .. include:: /includes/extracts/views-unsupported-projection-$elemMatch.rst
- You cannot specify a :query:`$text` query operator in an
:projection:`$elemMatch`.

## Examples

The examples on the :projection:`$elemMatch` projection operator assumes a collection `schools` with the following documents:

```javascript
{
 _id: 1,
 zipcode: "63109",
 students: [
              { name: "john", school: 102, age: 10 },
              { name: "jess", school: 102, age: 11 },
              { name: "jeff", school: 108, age: 15 }
           ]
},
{
 _id: 2,
 zipcode: "63110",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ],
 athletics: [ "swimming", "basketball", "football" ]
},
{
 _id: 3,
 zipcode: "63109",
 students: [
              { name: "ajax", school: 100, age: 7 },
              { name: "achilles", school: 100, age: 8 },
           ],
 athletics: [ "baseball", "basketball", "soccer" ]
},
{
 _id: 4,
 zipcode: "63109",
 students: [
              { name: "barney", school: 102, age: 7 },
              { name: "ruth", school: 102, age: 16 },
           ]
}
```

### Zipcode Search

The operation returns the following documents that have a `zipcode` value of `"63109"` and projects the `students` array using :projection:`$elemMatch`:

```javascript
{ "_id" : 1, "students" : [ { "name" : "john", "school" : 102, "age" : 10 } ] }
{ "_id" : 3 }
{ "_id" : 4, "students" : [ { "name" : "barney", "school" : 102, "age" : 7 } ] }
```

- For the document with `_id` equal to `1`, the `students`
array contains multiple elements with the `school` field equal to `102`. However, the :projection:`$elemMatch` projection returns only the first matching element from the array.

- The document with `_id` equal to `3` does not contain the
`students` field in the result since no element in its `students` array matched the :projection:`$elemMatch` condition.

### :projection:`$elemMatch` with Multiple Fields

The :projection:`$elemMatch` projection can specify criteria on multiple fields.

The operation returns the three documents that have a `zipcode` value of `"63109"`:

```javascript
{ "_id" : 1, "students" : [ { "name" : "jess", "school" : 102, "age" : 11 } ] }
{ "_id" : 3 }
{ "_id" : 4, "students" : [ { "name" : "ruth", "school" : 102, "age" : 16 } ] }
```

The document with `_id` equal to `3` does not contain the `students` field since no array element matched the :projection:`$elemMatch` criteria.

The argument to :projection:`$elemMatch` matches elements of the array that `$elemMatch` is projecting. If you specify an equality with a field name to `$elemMatch`, it attempts to match objects within the array. For example, `$elemMatch` attempts to match objects, instead of scalar values, within the array for the following in the projection:

The preceding examples return the documents that have a `zipcode` value of `"63109", but these documents include only the id` field because the projection operation found no matching elements.

The operation returns the three documents that have `zipcode` value of `"63109". The returned documents include the id` field and matching elements of the `athletics` array, if any.

```javascript
[
   { _id: 1 },
   { _id: 3, athletics: [ 'basketball' ] },
   { _id: 4 }
]
```

The document with `_id` equal to `3` is the only document that matched the :projection:`$elemMatch` criteria.

> **Seealso:** :projection:`$ (projection) <$>` operator
