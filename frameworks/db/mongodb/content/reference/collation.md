---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/collation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========

# Collation

Collation allows users to specify language-specific rules for string comparison, such as rules for lettercase and accent marks.

You can specify collation for a collection or a view, an index, or specific operations that support collation.

To specify collation when you query documents in the {+atlas+} UI, see :atlas:`Specify Collation </atlas-ui/documents/#specify-collation>`.

## Collation Document

A collation document has the following fields:

.. include:: /includes/extracts/collation-document.rst

Default collation parameter values vary depending on which locale you specify. For a complete list of default collation parameters and the locales they are associated with, see `Collation Default Parameters<collation-default-params>`.

## Operations that Support Collation

You can specify collation for the following operations:

> **Note:** .. include:: /includes/extracts/collation-single-per-operation.rst

.. include:: /includes/extracts/collation-operations-table.rst

Some index types do not support collation. See `collation-unsupported-index-types` for details.

## Behavior

### Local Variants

.. include:: /includes/collation-variants.rst

For a complete list of all collation locales and their variants, see `Collation Locales<collation-languages-locales>`.

### Collation and Views

.. include:: /includes/extracts/views-collation-behavior.rst

### Collation and Index Use

.. include:: /includes/extracts/collation-index-use.rst

Collation and Unsupported Index Types ``````````````````````````````````````

.. include::  /includes/extracts/collation-index-type-restrictions.rst

.. include:: /includes/extracts/collation-index-type-restrictions-addendum.rst

## Restrictions

### numericOrdering

When specifying the `numericOrdering` as `true` the following restrictions apply:

- Only contiguous non-negative integer substrings of digits are
considered in the comparisons.

`numericOrdering` does not support:

- `+`
- `-`
- decimal separators, like decimal points and decimal commas
- exponents
- Only Unicode code points in the Number or Decimal Digit (Nd) category
are treated as digits.

- If a digit length exceeds 254 characters, the excess characters are
treated as a separate number.

Consider a collection with the following string number and decimal values:

```javascript
db.c.insertMany(
  [
      { "n" : "1" },
      { "n" : "2" },
      { "n" : "2.1" },
      { "n" : "-2.1" },
      { "n" : "2.2" },
      { "n" : "2.10" },
      { "n" : "2.20" },
      { "n" : "-10" },
      { "n" : "10" },
      { "n" : "20" },
      { "n" : "20.1" }
  ]
)
```

The following :method:`find <db.collection.find()>` query uses a collation document containing the `numericOrdering` parameter:

```javascript
db.c.find(
   { }, { _id: 0 }
).sort(
  { n: 1 }
).collation( {
  locale: 'en_US',
  numericOrdering: true
} )
```

The operation returns the following results:

```javascript
[
    { n: '-2.1' },
    { n: '-10' },
    { n: '1' },
    { n: '2' },
    { n: '2.1' },
    { n: '2.2' },
    { n: '2.10' },
    { n: '2.20' },
    { n: '10' },
    { n: '20' },
    { n: '20.1' }
]
```

- `numericOrdering: true` sorts the string values in ascending
order as if they were numeric values.

- The two negative values `-2.1` and `-10` are not sorted in the
expected sort order because they have unsupported `-` characters.

- The value `2.2` is sorted before the value `2.10`, due to the fact
that the `numericOrdering` parameter does not support decimal values.

- As a result, `2.2` and `2.10` are sorted in lexicographic order.
## Contents

- Locales & Default Parameters </reference/collation-locales-defaults>

## Example

The following :method:`~db.collection.find()` operation uses collation to query the `movies` collection in the `sample_mflix` database:

The filter specifies a collation with `locale: "fr"` and `strength: 1`, which means the query ignores differences between case and letter variants. As a result, searching for `"les miserables"` returns documents whose titles contain both accented and non-accented variants.
