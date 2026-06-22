---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/model-data-for-keyword-search.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Model Data to Support Keyword Search

> **Note:** Keyword search is not the same as text search or full text
search, and does not provide stemming or other text-processing
features. See the `limit-keyword-indexes` section for more
information.
In 2.4, MongoDB provides a text search feature. See
`<index-type-text>` for more information.

If your application needs to perform queries on the content of a field that holds text you can perform exact matches on the text or use :query:`$regex` to use regular expression pattern matches. However, for many operations on text, these methods do not satisfy application requirements.

This pattern describes one method for supporting keyword search using MongoDB to support application search functionality, that uses keywords stored in an array in the same document as the text field. Combined with a `multi-key index <index-type-multikey>`, this pattern can support application's keyword search operations.

## Pattern

To add structures to your document to support keyword-based queries, create an array field in your documents and add the keywords as strings in the array. You can then create a `multi-key index <index-type-multi-key>` on the array and create queries that select values from the array.

> **Note:** several hundreds or thousands of keywords will incur greater
indexing costs on insertion.

## Limitations of Keyword Indexes

MongoDB can support keyword searches using specific data models and `multi-key indexes <index-type-multikey>`; however, these keyword indexes are not sufficient or comparable to full-text products in the following respects:

- Stemming. Keyword queries in MongoDB can not parse keywords for
root or related words.

- Synonyms. Keyword-based search features must provide support for
synonym or related queries in the application layer.

- Ranking. The keyword look ups described in this document do not
provide a way to weight results.

- Asynchronous Indexing. MongoDB builds indexes synchronously, which
means that the indexes used for keyword indexes are always current and can operate in real-time. However, asynchronous bulk indexes may be more efficient for some kinds of content and workloads.
