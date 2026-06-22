---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-use-text-operator.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You can use the :query:`$text` operator on a collection with a `text index <index-type-text>`.

`$text` tokenizes the search string using whitespace and most punctuation as delimiters, and performs a logical `OR` of all such tokens in the search string.

For example, you could use the following query to find all stores containing any terms from the list "coffee", "shop", and "java" in the `stores` `collection <text-index-eg>`:

```javascript
db.stores.find( { $text: { $search: "java coffee shop" } } )
```
