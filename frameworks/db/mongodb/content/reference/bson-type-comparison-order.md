---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/bson-type-comparison-order.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================

# Comparison/Sort Order

.. include:: /includes/fact-sort-order.rst

Aggregation expressions make comparisons across types. For more information, see `aggregation-comparison-operators`.

> **Note:** MongoDB enforces comparisons with `query-selectors-comparison`
only on documents where the BSON type of the target field
matches the query operand type through `type-bracketing`.

## Numeric Types

MongoDB treats some types as equivalent for comparison purposes. For instance, all numeric types are considered equivalent in comparisons.

## Strings

### Binary Comparison

By default, MongoDB uses the simple binary comparison to compare strings.

### Collation

.. include:: /includes/extracts/collation-description.rst

Collation specification has the following syntax:

.. include:: /includes/extracts/collation-document.rst

.. include:: /includes/extracts/collation-unspecified.rst

## Arrays

.. include:: /includes/sorting-arrays.rst

> **Note:** `query-selectors-comparison` enforce type-bracketing when
the query is an array. If the indexed value is an array,
the operator performs a type-bracketed comparison
element-wise over the indexed array.

## Objects

MongoDB's comparison of `BSON` objects uses the following order:

#. Recursively compare key-value pairs in the order that they appear within the BSON object.

#. Compare the field types. MongoDB uses the following comparison order for field types, from lowest to highest:

a. MinKey (internal type) #. Null #. Numbers (ints, longs, doubles, decimals) #. Symbol, String #. Object #. Array #. BinData #. ObjectId #. Boolean #. Date #. Timestamp #. Regular Expression #. JavaScript Code #. JavaScript Code with Scope #. MaxKey (internal type)

#. If the field types are equal, compare the `key field names <document-field-names>`.

#. If the key field names are equal, compare the field values.

#. If the field values are equal, compare the next key/value pair (return to step 1). An object without further pairs is less than an object with further pairs.

## Dates and Timestamps

Date objects sort before Timestamp objects.

## Non-existent Fields

The comparison treats a non-existent field as if it were null. A sort on the `a` field in documents `{ }` and `{ a: null }` would treat the documents as equivalent in sort order.

## BinData

MongoDB sorts `BinData` in the following order:

#. First, the length or size of the data.

#. Then, by the BSON one-byte subtype.

#. Finally, by the data, performing a byte-by-byte comparison on unsigned bytes.
