---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/update/rename.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# $rename (update operator)

## Definition

## Syntax

```javascript
{ $rename: { <field1>: <newName1>, <field2>: <newName2>, ... } }
```

The new field name must differ from the existing field name. To specify a `<field>` in an embedded document, use `dot notation`.

Consider the following example:

```javascript
db.students.updateOne(
   { _id: 1 }, { $rename: { 'nickname': 'alias', 'cell': 'mobile' } }
)
```

The preceding operation renames the `nickname` field to `alias` and the `cell` field to `mobile in a document where id` is 1.

## Behavior

When you run a `$rename` operation, MongoDB performs the following actions:

- Delete the old `<field>` and field with `<newName>` from the
document (using :update:`$unset`).

- Perform a :update:`$set` operation with `<newName>`, using the value
from `<field>`.

### Atomicity

Each document matched by an update command is updated in an individual operation. Update operations (like `$rename`) only guarantee atomicity on a single-document level.

### Field Order

The `$rename` operation might not preserve the order of the fields in the document.

### Update Processing Order

.. include:: /includes/fact-update-operator-processing-order.rst

### Rename Embedded Document Fields

The `$rename` operator can move fields into and out of embedded documents.

`$rename` does not work on embedded documents in arrays.

### Other Considerations

- If the document already has a field with the `<newName>`, the
:update:`$rename` operator removes that field and renames the specified `<field>` to `<newName>`.

- If the field to rename does not exist in a document, :update:`$rename`
does nothing.

- .. include:: /includes/extracts/update-operation-empty-operand-expressions-rename.rst
## Examples

Create the `students` collection:

```javascript
db.students.insertMany( [
   {
     "_id": 1,
     "alias": [ "The American Cincinnatus", "The American Fabius" ],
     "mobile": "555-555-5555",
     "nmae": { "first" : "george", "last" : "washington" }
   },
   {
     "_id": 2,
     "alias": [ "My dearest friend" ],
     "mobile": "222-222-2222",
     "nmae": { "first" : "abigail", "last" : "adams" }
   },
   {
     "_id": 3,
     "alias": [ "Amazing grace" ],
     "mobile": "111-111-1111",
     "nmae": { "first" : "grace", "last" : "hopper" }
   }
] )
```

The documents contain an error, `nmae` should be `name`. The examples in the following sections update the documents in the collection.

### Rename a Field

To rename a field, call the :update:`$rename` operator with the current name of the field and the new name:

```javascript
db.students.updateMany(
   { "nmae": { $ne: null } },
   { $rename: { "nmae": "name" } }
)
```

This operation checks for documents where the `nmae` field is not null and updates those documents to rename the `nmae` field to `name`:

```javascript
{
  "_id": 1,
  "alias": [ "The American Cincinnatus", "The American Fabius" ],
  "mobile": "555-555-5555",
  "name": { "first" : "george", "last" : "washington" }
}

{
   "_id" : 2,
   "alias" : [ "My dearest friend" ],
   "mobile" : "222-222-2222",
   "name" : { "first" : "abigail", "last" : "adams" }
}

{ 
   "_id" : 3,
  "alias" : [ "Amazing grace" ],
  "mobile" : "111-111-1111",
  "name" : { "first" : "grace", "last" : "hopper" }
}
```

### Rename a Field in an Embedded Document

To rename a field in an embedded document, call the :update:`$rename` operator using the `dot notation <document-dot-notation>` to refer to the field. If the field is to remain in the same embedded document, also use the dot notation in the new name, as in the following:

```javascript
db.students.updateOne( { _id: 1 }, { $rename: { "name.first": "name.fname" } } )
```

This operation renames the embedded field `first` to `fname`:

```javascript
{
  _id: 1,
  alias: [ 'The American Cincinnatus', 'The American Fabius' ],
  mobile: '555-555-5555',
  name: { last: 'washington', fname: 'george' }
}
```

### Rename a Field That Does Not Exist

When renaming a field and the existing field name refers to a field that does not exist, the :update:`$rename` operator does nothing, as in the following:

```javascript
db.students.updateOne( { _id: 1 }, { $rename: { 'wife': 'spouse' } } )
```

This operation does nothing because there is no field named `wife`.

> **Seealso:** - :method:`db.collection.updateMany()`
- :method:`db.collection.findAndModify()`
