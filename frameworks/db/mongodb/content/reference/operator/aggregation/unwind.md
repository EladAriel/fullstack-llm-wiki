---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/unwind.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $unwind (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

You can pass a field path operand or a document operand to unwind an array field.

### Field Path Operand

You can pass the array field path to :pipeline:`$unwind`. When using this syntax, :pipeline:`$unwind` does not output a document if the field value is null, missing, or an empty array.

```javascript
{ $unwind: <field path> }
```

When you specify the field path, prefix the field name with a dollar sign `$` and enclose in quotes.

### Document Operand with Options

You can pass a document to :pipeline:`$unwind` to specify various behavior options.

```javascript
{
  $unwind:
    {
      path: <field path>,
      includeArrayIndex: <string>,
      preserveNullAndEmptyArrays: <boolean>
    }
}
```

## Behaviors

### Non-Array Field Path

When the value at `path` does not resolve to an array, `$unwind` behaves as follows:

- If the value is not missing, not `null`, and not an empty array,
`$unwind` outputs a single document using the value as-is.

- If `includeArrayIndex` is specified, the index is `0` for
array inputs and `null` for non-array inputs. Documents later in the list have an index greater than `0`.

- If the value is missing, `null`, or an empty array, `$unwind`
follows the `preserveNullAndEmptyArrays <unwind-preserveNullAndEmptyArrays>` option. When `includeArrayIndex` is specified and the document is preserved, the index is `null`.

### Missing Field

If you specify a path for a field that does not exist in an input document or the field is an empty array, :pipeline:`$unwind`, by default, ignores the input document and will not output documents for that input document.

To output documents where the array field is missing, null or an empty array, use the `preserveNullAndEmptyArrays <unwind-preserveNullAndEmptyArrays>` option.

## Examples

## Learn More

To learn more about related methods, see the :pipeline:`$group`, :group:`$sum`, and :expression:`$multiply` guides.

To see how to use :pipeline:`$unwind` in a full example, see the `agg-example-unpack-arrays` tutorial.
