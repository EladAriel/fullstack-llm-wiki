---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.pretty.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
