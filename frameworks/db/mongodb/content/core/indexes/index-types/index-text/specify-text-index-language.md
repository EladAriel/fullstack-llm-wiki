---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/specify-text-index-language.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Specify Language for Text Indexes on Self-Managed MongoDB

.. include:: /includes/fact-fts-language-analyzers.rst

By default, the `default_language` for text indexes is `english`. To improve the performance of non-English `$text` queries, you can specify a different default language associated with your text index.

The default language associated with the indexed data determines the suffix stemming rules. The default language also determines which language-specific stop words (for example, `the`, `an`, `a`, and `and` in English) are not indexed.

To specify a different language, use the `default_language` option when creating the text index. To see the languages available for text indexing, see `text-search-languages`. Your operation should resemble this prototype:

```javascript
db.<collection>.createIndex( 
   { <field>: "text" }, 
   { default_language: <language> } 
)
```

.. include:: /includes/fact-text-search-language-none.rst

## Before You Begin

Create a `quotes` collection that contains the following documents with a Spanish text field:

```javascript
db.quotes.insertMany( [
   {
      _id: 1,
      quote : "La suerte protege a los audaces."
   },
   {
      _id: 2,
      quote: "Nada hay más surrealista que la realidad."
   },
   {
      _id: 3,
      quote: "Es este un puñal que veo delante de mí?"
   },
   {
      _id: 4,
      quote: "Nunca dejes que la realidad te estropee una buena historia."
   } 
] )
```

## Procedure

The following operation creates a text index on the `quote` field and sets the `default_language` to `spanish`:

```javascript
db.quotes.createIndex( 
   { quote: "text" },
   { default_language: "spanish" }
)
```

## Results

The resulting index supports `$text` queries on the `quote` field with Spanish-language suffix stemming rules. For example, the following query searches for the keyword `punal` in the `quote` field:

```javascript
db.quotes.find(
   { 
      $text: { $search: "punal" }
   }
)
```

Output:

```javascript
[
   {
      _id: 3,
      quote: "Es este un puñal que veo delante de mí?"
   }
]
```

Although the `$search` value is set to `punal`, the query will return the document containing the word `puñal` because text indexes are `diacritic insensitive <text-index-diacritic-insensitivity>`.

The index also ignores language-specific stop words. For example, although the document with `_id: 2` contains the word `hay`, the following query does not return any documents. `hay` is classified as a Spanish stop word, meaning it is not included in the text index.

```javascript
db.quotes.find(
   { 
      $text: { $search: "hay" }
   }
)
```

## Learn More

- To create a text index for a collection containing text in
multiple languages, see `multiple-language-text-index`.

- To learn about other text index properties, see
`text-index-properties`.

## Contents

- Multiple Languages </core/indexes/index-types/index-text/specify-language-text-index/create-text-index-multiple-languages>
- Field Use </core/indexes/index-types/index-text/specify-language-text-index/use-any-field-to-specify-language>
