---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-text/specify-language-text-index/create-text-index-multiple-languages.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================================

# Create a Multi-Language Text Index on Self-Managed Deployments

> **Note:** :atlas:`{+fts+} </atlas-search/>` offers advanced full-text
search capabilities, including `multi analyzers <ref-multi-analyzers>`.
We recommend using `{+fts+} indexes <fts-manage-indexes>` instead of
text indexes.

You can create a text index to improve the performance of text queries run on a collection containing documents or embedded documents with text in multiple languages.

If a collection contains documents or embedded documents that are in multiple different languages, include a field named `language` and specify the language for those documents as the field value. To see the languages available for text indexing, see `text-search-languages`.

Your insert operation should resemble this example to support text indexing for multiple languages:

```javascript
db.<collection>.insertOne( 
   { 
      <field>: <value>,
      language: <language> 
   } 
)
```

## Before You Begin

Create a `quotes` collection that contains multi-language documents that include the `language` field:

```javascript
db.quotes.insertMany( [
   {
      _id: 1,
      language: "portuguese",
      original: "A sorte protege os audazes.",
      translation:
        [
           {
              language: "english",
              quote: "Fortune favors the bold."
           },
           {
              language: "spanish",
              quote: "La suerte protege a los audaces."
           }
       ]
   },
   {
      _id: 2,
      language: "spanish",
      original: "Nada hay más surrealista que la realidad.",
      translation:
         [
           {
             language: "english",
             quote: "There is nothing more surreal than reality."
           },
           {
             language: "french",
             quote: "Il n'y a rien de plus surréaliste que la réalité."
           }
         ]
   },
   {
      _id: 3,
      original: "Is this a dagger which I see before me?",
      translation:
      {
         language: "spanish",
         quote: "Es este un puñal que veo delante de mí."
      }
   } 
] )
```

## Procedure

The following operation creates a text index on the `original` and `translation.quote` fields:

```javascript
db.quotes.createIndex({ original: "text", "translation.quote": "text", "default_language" : "fr" })
```

> **Note:** English is the default language for indexes. If you do not specify the
`default_language <createIndexes-default-language>`, your query must
specify the language with the `$language <language-field>` parameter.
For more information, refer to `<specify-default-text-index-language>`.

## Results

The resulting index supports `$text` queries for the documents and embedded documents containing the `original` and `translation.quote` fields. The text index follows different suffix stemming rules, and ignores stop words specific to each language, based on the value in the `language` field.

For example, the following query searches for the `french` word `réalité`.

```javascript
db.quotes.find(
   { $text: 
      { $search: "réalité" }
   }
)
```

Output:

```javascript
[
   {
      _id: 2,
      language: 'spanish',
      original: 'Nada hay más surrealista que la realidad.',
      translation: [
         {
            language: 'english',
            quote: 'There is nothing more surreal than reality.'
         },
         {
            language: 'french',
            quote: "Il n'y a rien de plus surréaliste que la réalité."
         }
      ]
   }
]
```

For embedded documents that do not contain the `language` field,

- If the enclosing document contains the `language` field, then the index uses
the document's language for the embedded documents.

- Otherwise, the index uses the default language for the embedded documents.
For documents that do not contain the `language` field, the index uses the default language, which is English.

## Learn More

- To specify the text index language in a field other than `language`,
see `text-index-specify-language-in-field`.

- To learn how to specify the default language for a text index, see
`specify-default-text-index-language`.

- To learn about other text index properties, see `text-index-properties`.
