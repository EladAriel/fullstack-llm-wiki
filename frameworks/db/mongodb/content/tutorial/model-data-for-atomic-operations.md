---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/model-data-for-atomic-operations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# Model Data for Atomic Operations

Although MongoDB supports `multi-document transactions <transactions>` for replica sets and sharded clusters, for many scenarios, the denormalized data model, as discussed on this page, will continue to be optimal for your data and use cases.

## Pattern

In MongoDB, a write operation on a single document is atomic. For fields that must be updated together, embedding the fields within the same document ensures that the fields can be updated atomically.

For example, consider a situation where you need to maintain information on books, including the number of copies available for checkout as well as the current checkout information.

The available copies of the book and the checkout information should be in sync. As such, embedding the `available` field and the `checkout` field within the same document ensures that you can update the two fields atomically.

```javascript
{
    _id: 123456789,
    title: "MongoDB: The Definitive Guide",
    author: [ "Kristina Chodorow", "Mike Dirolf" ],
    published_date: ISODate("2010-09-24"),
    pages: 216,
    language: "English",
    publisher_id: "oreilly",
    available: 3,
    checkout: [ { by: "joe", date: ISODate("2012-10-15") } ]
}
```

Then to update with new checkout information, you can use the :method:`db.collection.updateOne()` method to atomically update both the `available` field and the `checkout` field:

```javascript
db.books.updateOne (
   { _id: 123456789, available: { $gt: 0 } },
   {
     $inc: { available: -1 },
     $push: { checkout: { by: "abc", date: new Date() } }
   }
)
```

The operation returns a document that contains information on the status of the operation:

```javascript
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
```

The `matchedCount` field shows that `1` document matched the update condition, and `modifiedCount` shows that the operation updated `1` document.

If no document matched the update condition, then `matchedCount` and `modifiedCount` would be `0` and would indicate that you could not check out the book.
