---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/query/text.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# $text (query predicate operator)

.. include:: /includes/extracts/fact-text-search-legacy-atlas.rst

This page describes the `$text` operator for self-managed deployments.

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

A `$text` expression has the following syntax:

```javascript
{
  $text: {
    $search: <string>,
    $language: <string>,
    $caseSensitive: <boolean>,
    $diacriticSensitive: <boolean>
  }
}
```

The `$text` operator accepts these fields:

By default, `$text` does not sort results by score. See `text-operator-text-score` for details on score sorting.

## Behavior

### Restrictions

- A query can specify only one `$text` expression.
- `$text` cannot appear in :query:`$nor` expressions.
- `$text` cannot appear in :query:`$elemMatch` query or
projection expressions.

- All :query:`$or` clauses must be indexed to use `$text`.
- .. include:: /includes/fact-hint-text-query-restriction.rst
- Queries with `$text` cannot use :operator:`$natural` sort.
- .. include:: /includes/fact-special-indexes-and-text.rst
- .. include:: /includes/extracts/views-unsupported-text-search.rst
- `Stable API <stable-api>` V1 does not support `$text`
for index creation.

If using the `$text` operator in aggregation, the following restrictions also apply.

.. include:: /includes/list-text-search-restrictions-in-agg.rst

### `$search` Field

In the `$search` field, specify the words that MongoDB uses to query the `text index <index-type-text>`.

> **Note:** The `$search` field differs from the MongoDB Atlas :atlas:`$search
aggregation stage </reference/atlas-search/query-syntax/>`.
The `$search` stage provides full-text search and is
available only on MongoDB Atlas.

Exact Strings `````````````

To match an exact multi-word string instead of individual terms, enclose the string in escaped double quotes (`\"`): as in:

```javascript
"\"ssl certificate\""
```

.. include:: /includes/fact-text-search-multiword-and-term.rst

For example, this `$search` string returns documents with the exact string `"ssl certificate"`:

```javascript
"\"ssl certificate\" authority key"
```

Negations `````````

Prefix a word with a hyphen-minus (`-`) to negate it:

- Negated words exclude documents that contain the negated word
from the result set.

- A string with only negated words matches no documents.
- Hyphenated words like `pre-market` are not negations.
MongoDB treats the hyphen as a delimiter. To negate `market`, use `pre -market`.

MongoDB applies all negations to the operation with logical `AND`.

### Match Operation

Stop Words ``````````

MongoDB ignores language-specific stop words such as `the` and `and` in English.

Stemmed Words `````````````

With case and diacritic insensitivity, `$text` matches the complete stemmed word. If a document field contains `blueberry`, a `$search` term of `blue` does not match. However, `blueberry` or `blueberries` do match.

#### Case Sensitivity and Stemmed Words

With case sensitivity enabled (`$caseSensitive: true`), if the suffix stem contains uppercase letters, `$text` matches the exact word.

#### Diacritic Sensitivity and Stemmed Words

With `diacritic sensitivity <text-operator-diacritic-sensitivity>` enabled (`$diacriticSensitive: true`), if the suffix stem contains diacritic marks, `$text` matches the exact word.

### Case Insensitivity

`$text` defaults to the case insensitivity of the `text <index-type-text>` index:

- The version 3 `text index <text-index-case-insensitivity>` is
case insensitive for Latin characters with or without diacritics and non-Latin alphabets like Cyrillic.

- Earlier versions are case insensitive for Latin characters
without diacritics (`[A-z]`).

Enabling Case Sensitivity `````````````````````````

Specify `$caseSensitive: true` to enable case sensitivity when the text index is case insensitive.

Case Sensitivity Process ````````````````````````

When `$caseSensitive: true` and the text index is case insensitive, `$text`:

- Queries the text index for case-insensitive and
diacritic-insensitive matches.

- Filters results to return only documents matching the specified
case.

When `$caseSensitive: true` and the suffix stem contains uppercase letters, `$text` matches the exact word.

Enabling `$caseSensitive: true` may reduce performance.

### Diacritic Insensitivity

`$text` defaults to the diacritic insensitivity of the `text <index-type-text>` index:

- Version 3 :ref:`text index
<text-index-diacritic-insensitivity>` is diacritic insensitive. The index does not distinguish between characters with diacritic marks and their non-marked counterparts (`é`, `ê`, `e`).

- Earlier versions are diacritic sensitive.
Enabling Diacritic Sensitivity ``````````````````````````````

Specify `$diacriticSensitive: true` to enable diacritic sensitivity with version 3 text indexes.

Earlier text index versions are always diacritic sensitive, so `$diacriticSensitive` has no effect.

Diacritic Sensitivity Process `````````````````````````````

With version 3 text indexes and `$diacriticSensitive: true`, `$text`:

- Queries the diacritic-insensitive text index.
- Filters results to return only documents matching the diacritic
marks in the specified terms.

Enabling `$diacriticSensitive: true` may reduce performance.

With earlier text index versions, `$diacriticSensitive: true` queries the already diacritic-sensitive text index.

When `$diacriticSensitive: true` and the suffix stem contains diacritic marks, `$text` matches the exact word.

> **Seealso:** `match-operation-stemmed-words`

### Text Score

.. include:: /includes/fact-text-search-score.rst

### Memory Limits

.. versionchanged:: 8.3

.. include:: /includes/fact-text-search-spilling.rst

## Examples

.. include:: /includes/sample-data-usage.rst

The examples assume a `version 3 text <index-type-text>` index on the `title` and `fullplot` fields:

### Search for a Single Word

This example specifies `baseball` in the `$search` string. The query returns documents containing the stemmed version of `baseball` in the indexed `title` or `fullplot` fields:

### Match Any Search Term

A space-delimited `$search` string performs a logical `OR` on each term. MongoDB returns documents containing any of the terms.

This example specifies two space-delimited terms. The query returns documents containing the stemmed versions of `baseball` **or** `colorado` in the indexed `title` or `fullplot` fields:

### Search for an Exact String

Escape the quotes to match an exact multi-word string.

This example matches the exact phrase `ken burns`:

This example performs a logical OR of two exact strings:

### Exclude Documents That Contain a Term

Prefix a term with `-` to exclude documents containing that term.

This example matches documents containing `baseball` or `colorado` but not `sport` (stemmed versions):

### Relevance Score Examples

Return the Relevance Score ``````````````````````````

This example queries for `baseball` and uses :expression:`$meta` to append the relevance score to each matching document. The returned document includes a `score` field with the relevance score:

Return Top 2 Matching Documents ```````````````````````````````

Use :method:`~cursor.limit()` with :method:`~cursor.sort()` to return the top matching documents.

This example queries for `baseball` **or** `colorado`, sorts by descending score, and limits results to the top two documents:

Combine $text with Other Query and Sort Operations ``````````````````````````````````````````````````

This example matches documents where `runtime` is greater than `1000` and the indexed fields contain `baseball` or `colorado`. It sorts by ascending `year`, then descending relevance score:

### Query a Different Language

The rest of the examples on this page use an `articles` collection with a `version 3 text <index-type-text>` index on `subject`:

The collection contains the following documents:

Use `$language` to specify the language that determines stop words, stemmer, and tokenizer rules for the `$search` string.

.. include:: /includes/fact-text-search-language-none.rst

This example specifies `es` (Spanish) as the language:

You can also specify languages by name, such as `spanish`. See `text-search-languages` for supported languages.

### Sort by Relevance Score

.. include:: /includes/extracts/4.4-changes-projection-sort-meta-list.rst

### Case and Diacritic Insensitivity

`$text` defaults to the case and diacritic insensitivity of the text index. Version 3 text indexes are diacritic insensitive and case insensitive for Latin characters with diacritics and non-Latin alphabets like Cyrillic. See `text Index Case Insensitivity <text-index-case-insensitivity>` and `text Index Diacritic Insensitivity <text-index-diacritic-insensitivity>`.

This example performs a case and diacritic insensitive query. Using version 3 text indexes, the query matches documents containing the stemmed versions of the search terms:

Earlier text index versions would not match any documents.

### Case Sensitivity

Enable case sensitivity with `$caseSensitive: true`. This may reduce performance.

Case-Sensitive Term Search ``````````````````````````

This example performs a case-sensitive query for `Coffee`:

Case-Sensitive Exact String Search ``````````````````````````````````

This example performs a case-sensitive query for an exact multi-word string:

Case-Sensitive Negated Term Search ``````````````````````````````````

You can use case sensitivity with negated terms (terms prefixed with `-`).

This example performs a case-sensitive query for documents containing `Coffee` but not `shop` (stemmed versions):

### Diacritic Sensitivity

Enable diacritic sensitivity with version 3 `text <index-type-text>` indexes using `$diacriticSensitive: true`. This may reduce performance.

Diacritic-Sensitive Term Search ```````````````````````````````

This example performs a diacritic-sensitive query for `CAFÉ` (stemmed version):

Diacritic-Sensitive Negated Term Search ```````````````````````````````````````

You can use diacritic sensitivity with negated terms (terms prefixed with `-`).

This example performs a diacritic-sensitive query for documents containing `leches` but not `cafés` (stemmed versions):

> **Seealso:** - `index-type-text`
- `match-operation-stemmed-words`
- `text-operator-exact-string`
- `text-operator-term-negation`
- `text-operator-case-sensitivity`
- `case-sensitivity-and-stemming`
- `text-operator-diacritic-sensitivity`
- `diacritic-sensitivity-and-stemming`
- :expression:`$meta`
- `text-agg`
