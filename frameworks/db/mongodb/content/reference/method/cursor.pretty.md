---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.pretty.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# cursor.pretty() (mongosh method)

## Definition

## Behavior

The :method:`~cursor.pretty()` method:

- Does not change the output format in :binary:`~bin.mongosh`.
- Changes the output format in the `legacy mongo shell<mongo>`.
## Examples

Consider the following document:

```javascript
db.books.insertOne({
    "_id" : ObjectId("54f612b6029b47909a90ce8d"),
    "title" : "A Tale of Two Cities",
    "text" : "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...",
    "authorship" : "Charles Dickens"})
```

By default, :method:`db.collection.find()` returns data in a dense format:

```javascript
db.books.find()
{ "_id" : ObjectId("54f612b6029b47909a90ce8d"), "title" : "A Tale of Two Cities", "text" : "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...", "authorship" : "Charles Dickens" }
```

By using :method:`cursor.pretty()` you can set the cursor to return data in a format that is easier to read:

```javascript
db.books.find().pretty()
{
    "_id" : ObjectId("54f612b6029b47909a90ce8d"),
    "title" : "A Tale of Two Cities",
    "text" : "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness...",
    "authorship" : "Charles Dickens"
}
```
