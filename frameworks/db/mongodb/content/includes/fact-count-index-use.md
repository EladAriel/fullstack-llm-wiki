---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-count-index-use.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Consider a collection with the following index:

```javascript
{ a: 1, b: 1 }
```

When performing a count, MongoDB can return the count using only the index if:

- the query can use an index,
- the query only contains conditions on the keys of the index, and
- the query predicates access a single contiguous range of index keys.
For example, the following operations can return the count using only the index:

```javascript
db.collection.find( { a: 5, b: 5 } ).count()
db.collection.find( { a: { $gt: 5 } } ).count()
db.collection.find( { a: 5, b: { $gt: 10 } } ).count()
```

If, however, the query can use an index but the query predicates do not access a single contiguous range of index keys or the query also contains conditions on fields outside the index, then in addition to using the index, MongoDB must also read the documents to return the count.

```javascript
db.collection.find( { a: 5, b: { $in: [ 1, 2, 3 ] } } ).count()
db.collection.find( { a: { $gt: 5 }, b: 5 } ).count()
db.collection.find( { a: 5, b: 5, c: 5 } ).count()
```

In such cases, during the initial read of the documents, MongoDB pages the documents into memory such that subsequent calls of the same count operation will have better performance.
