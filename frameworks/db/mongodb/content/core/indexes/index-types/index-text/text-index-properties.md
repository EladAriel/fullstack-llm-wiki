---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/text-index-properties.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# Text Index Properties on Self-Managed Deployments

> **Note:** MongoDB offers an improved full-text search solution, :atlas:`{+fts+}
</atlas-search/>`, and a semantic search solution, :atlas:`{+avs+}
</atlas-vector-search/>`. We recommend using :ref:`{+fts+} indexes
<fts-manage-indexes>` or `{+avs+} indexes <avs-types-vector-search>`
instead of text indexes.

This page describes the behavior of `version 3 <text-index-versions>` text indexes.

## Case Insensitivity

Text indexes are case insensitive. The text index does not distinguish between capitalized and lower-case characters, such as `e` and `E`.

Text indexes support case foldings as specified in [Unicode 8.0 Character Database Case Folding](http://www.unicode.org/Public/8.0.0/ucd/CaseFolding.txt):

- Common C
- Simple S
- Special T for Turkish languages
- Characters with diacritics, such as `é` and `É`
- Characters from non-Latin alphabets, such as `И` and `и` in the
Cyrillic alphabet.

`Previous text index versions <text-index-versions>` are only case insensitive for non-diacritic Latin characters `[A-z]`. Previous text index versions treat all other characters as distinct.

## Diacritic Insensitivity

Text indexes are diacritic insensitive. The text index does not distinguish between characters that contain diacritical marks and their non-marked counterparts, such as `é`, `ê`, and `e`. More specifically, the text index strips the markings categorized as diacritics in the [Unicode 8.0 Character Database Prop List](http://www.unicode.org/Public/8.0.0/ucd/PropList.txt).

`Previous versions <text-index-versions>` of the text index treat characters with diacritics as distinct.

## Tokenization Delimiters

For tokenization, text indexes use the delimiters categorized under `Dash`, `Hyphen`, `Pattern_Syntax`, `Quotation_Mark`, `Terminal_Punctuation`, and `White_Space` in the [Unicode 8.0 Character Database Prop List](http://www.unicode.org/Public/8.0.0/ucd/PropList.txt).

For example, in the string `Il a dit qu'il «était le meilleur joueur du monde»`, the quotation marks (`«`, `»`) and spaces are delimiters.

`Previous versions <text-index-versions>` of the index treat `«` as part of the term `«était` and `»` as part of the term `monde»`.

## Index Entries

Text indexes tokenize and stem the terms in the indexed fields for the index entries. The index uses simple `language-specific <text-index-supported-languages>` suffix stemming. For each document in the collection, the text index stores one index entry for each unique stemmed term in each indexed field.

## Supported Languages and Stop Words

MongoDB supports `$text` queries for various languages. Text indexes use simple language-specific suffix stemming. Text indexes also drop language-specific stop words such as `the`, `an`, `a`, and `and` in English. For a list of the supported languages, see `text-search-languages`.

To specify a language for the text index, see `specify-text-index-language`.

## Sparse Property

Text indexes are always `sparse <index-type-sparse>`. When you create a text index, MongoDB ignores the `sparse` option.

If an existing or newly inserted document lacks a text index field (or the field is null or an empty array), MongoDB does not add a text index entry for the document.

## Learn More

To learn about text index restrictions, see `text-index-versions`.
