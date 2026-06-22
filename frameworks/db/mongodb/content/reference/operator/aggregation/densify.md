---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/densify.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# $densify (aggregation stage)

## Definition

## Syntax

The :pipeline:`$densify` stage has this syntax:

```none
{
   $densify: {
      field: <fieldName>,
      partitionByFields: [ <field 1>, <field 2> ... <field n> ],
      range: {
         step: <number>,
         unit: <time unit>,
         bounds: < "full" || "partition" > || [ < lower bound >, < upper bound > ]
      }
   }
}
```

The :pipeline:`$densify` stage takes a document with these fields:

## Behavior and Restrictions

### `field` Restrictions

For documents that contain the specified `field <densify-field>`, :pipeline:`$densify` errors if:

- Any document in the collection has a `field` value  of type date and
the `unit <densify-unit>` field is not specified.

- Any document in the collection has a `field` value  of type numeric
and the `unit <densify-unit>` field is specified.

- The `field` name begins with `$`. You must rename the field if
you want to densify it. To rename fields, use :pipeline:`$project`.

- .. versionadded:: 8.1
`field` shares its prefix with any field in the `partitionByFields` array. For example, the following combinations of `field` and `partitionByFields` result in an error:

.. include:: /includes/densify-validation-examples.rst

### `partitionByFields` Restrictions

:pipeline:`$densify` errors if any field name in the `partitionByFields <densify-partition-by-fields>` array:

- Evaluates to a non-string value.
- Begins with `$`.
### `range.bounds` Behavior

If `range.bounds <densify-bounds>` is an array:

- The lower bound indicates the start value for the added
documents, irrespective of documents already in the collection.

- The lower bound is inclusive.
- The upper bound is exclusive.
- :pipeline:`$densify` does not filter out documents with
`field <densify-field>` values outside of the specified bounds.

> **Note:** Starting in MongoDB 8.0, :pipeline:`$densify` treats bounds with an equal
lower and upper bound as an empty set and does not generate a document
with the bound as the field value.
In prior versions, :pipeline:`$densify` treats bounds with an equal lower
and upper bound as a closed interval and generates a document with the
bound value as a field value if the collection does not already contain
a document with the bound value.
For example, a `range.bounds <densify-bounds>` of `[10, 10]` generates an extra document
with field value `10` in versions prior to 8.0, but does not generate such a
document in 8.0 and later.

### Order of Output

:pipeline:`$densify` does not guarantee sort order of the documents it outputs.

To guarantee sort order, use :pipeline:`$sort` on the field you want to sort by.

## Examples
