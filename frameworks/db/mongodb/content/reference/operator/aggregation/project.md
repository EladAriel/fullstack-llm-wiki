---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/project.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $project (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :pipeline:`$project` stage has the following prototype form:

```javascript
{ $project: { <specification(s)> } }
```

The :pipeline:`$project takes a document that can specify the inclusion of fields, the suppression of the id` field, the addition of new fields, and the resetting of the values of existing fields. Alternatively, you may specify the exclusion of fields.

The :pipeline:`$project` specifications have the following forms:

## Behavior

### Include Fields

- The `_id` field is, by default, included in the output documents.
To include any other fields from the input documents in the output documents, you must explicitly specify the inclusion in :pipeline:`$project`.

- If you specify an inclusion of a field that does not exist in the
document, :pipeline:`$project` ignores that field inclusion and does not add the field to the document.

### `_id` Field

By default, the `_id field is included in the output documents. To exclude the id field from the output documents, you must explicitly specify the suppression of the id` field in :pipeline:`$project`.

### Exclude Fields

If you specify the exclusion of a field or fields, all other fields are returned in the output documents.

```javascript
{ $project: { "<field1>": 0, "<field2>": 0, ... } } // Return all but the specified fields
```

If you specify the exclusion of a field other than `_id`, you cannot employ any other :pipeline:`$project` specification forms: i.e. if you exclude fields, you cannot also specify the inclusion of fields, reset the value of existing fields, or add new fields. This restriction does not apply to conditional exclusion of a field using the :variable:`REMOVE` variable.

See also the :pipeline:`$unset` stage to exclude fields.

Exclude Fields Conditionally ````````````````````````````

You can use the variable :variable:`REMOVE` in aggregation expressions to conditionally suppress a field. For an example, see `remove-example`.

### Add New Fields or Reset Existing Fields

> **Note:** MongoDB also provides :pipeline:`$addFields` to add new fields to
the documents.

To add a new field or to reset the value of an existing field, specify the field name and set its value to some expression. For more information on expressions, see `aggregation-expressions`.

Literal Values ``````````````

To set a field value directly to a numeric or boolean literal, as opposed to setting the field to an expression that resolves to a literal, use the :expression:`$literal` operator. Otherwise, :pipeline:`$project` treats the numeric or boolean literal as a flag for including or excluding the field.

Field Rename ````````````

By specifying a new field and setting its value to the field path of an existing field, you can effectively rename a field.

New Array Fields ````````````````

The :pipeline:`$project` stage supports using the square brackets `[]` to directly create new array fields. If you specify array fields that do not exist in a document, the operation substitutes `null` as the value for that field. For an example, see `example-project-new-array-fields`.

.. include:: /includes/project-stage-and-array-index.rst

### Embedded Document Fields

When projecting or adding/resetting a field within an embedded document, you can either use `dot notation`, as in

```javascript
"contact.address.country": <1 or 0 or expression>
```

Or you can nest the fields:

```javascript
contact: { address: { country: <1 or 0 or expression> } }
```

When nesting the fields, you cannot use dot notation inside the embedded document to specify the field, e.g. `contact: { "address.country": <1 or 0 or expression> }` is invalid.

Path Collision Errors in Embedded Fields ````````````````````````````````````````

You cannot specify both an embedded document and a field within that embedded document in the same projection.

The following :pipeline:`$project` stage fails with a `Path collision` error because it attempts to project both the embedded `contact` document and the `contact.address.country` field:

```javascript
{ $project: { contact: 1, "contact.address.country": 1 } }
```

The error occurs regardless of the order in which the parent document and embedded field are specified. The following :pipeline:`$project` fails with the same error:

```javascript
{ $project: { "contact.address.country": 1, contact: 1 } }
```

### `$project` Stage Placement

.. include:: /includes/aggregation/fact-project-stage-placement.rst

## Considerations

### Empty Specification

MongoDB returns an error if the :pipeline:`$project` stage is passed an empty document.

For example, running the following pipeline produces an error:

```javascript
db.myCollection.aggregate( [ {
   $project: { }
} ] )
```

### Array Index

.. include:: /includes/project-stage-and-array-index.rst

## Examples

.. include:: /includes/sample-data-usage.rst

## Learn More

For more information and detailed explanations of common aggregation tasks, see the `aggregation-complete-examples`.

To learn more about the methods on this page, see the following guides:

- :expression:`$eq`
- :expression:`$cond`
- :expression:`$arrayElemAt`
- :expression:`$concatArrays`
- :variable:`REMOVE`
