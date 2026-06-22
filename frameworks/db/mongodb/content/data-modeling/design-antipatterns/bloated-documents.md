---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-antipatterns/bloated-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Bloated Documents

Storing data fields that are related to each other but not accessed together can create bloated documents that lead to excessive RAM and bandwidth usage. The `working set`, consisting of frequently accessed data and indexes, is stored in the RAM allotment. When the working set fits in RAM, MongoDB can query from memory instead of from disk, which improves performance. However, if documents are too large, the working set might not fit into RAM, causing performance to degrade as MongoDB has to access data from disk.

To prevent bloated documents, restructure your schema with smaller documents and use `document references <data-modeling-referencing>` to separate fields that aren't returned together. This approach reduces the working set size and improves performance.

## About this Task

Consider the following schema that contains book information used on a bookstore website's main page. The main page only displays the book title, author, and front cover image. You must click on the book to see additional details.

```javascript
{  
   title: "Tale of Two Cities",
   author: "Charles Dickens",
   genre: "Historical Fiction",
   cover_image: "<url>",
   year: 1859,
   pages: 448,
   price: 15.99,
   description: "A historical novel set during the French Revolution.
}
```

In the current schema, to display the information for the website's main page, all of the book information must be queried. To reduce document size and streamline queries, you can split the large document into two smaller collections.

## Example

In the following example, the book information is split into two collections: `mainBookInfo` and `additionalBookDetails`.

- The `mainBookInfo` collection contains the information displayed on
the website's main page.

- The `additionalBookDetails` collection contains extra details revealed
after a user clicks on the book.

The `mainBookInfo` collection:

```javascript
db.mainBookInfo.insertOne(
   {
      _id: 1234,
      title: "Tale of Two Cities",
      author: "Charles Dickens",
      genre: "Historical Fiction",
      cover_image: "<url>"
   }
)
```

The `additionalBookDetails` collection:

```javascript
db.additionalBookDetails.insertOne(
   {  
      title: "Tale of Two Cities",
      bookId: 1234,
      year: 1859,
      pages: 448,
      price: 15.99,
      description: "A historical novel set during the French Revolution."
   }
)
```

The two collections are linked by the `_id` field in the `mainBookInfo` collection and the `bookId` field in the `additionalBookDetails` collection. On the home page, only the `mainBookInfo` collection is used to provide the necessary information. When a user selects a book to learn more about, the website queries the `additionalBookDetails collection using the id` field to match with the `bookId` field.

By splitting the information into two collections, you ensure that your documents do not grow too large and exceed RAM allotment.

Join Collections with $lookup `````````````````````````````

To join the data from the `mainBookInfo` collection and the `additionalBookDetails` collection, the application needs to perform a :pipeline:`$lookup` operation.

The following aggregation operation joins the `mainBookInfo` and `additionalBookDetails` collection from the previous example.

```javascript
db.mainBookInfo.aggregate( [ 
   {
      $lookup: {
         from: "additionalBookDetails",
         localField: "_id", 
         foreignField: "bookId",
         as: "details"
      }
   },
   {
      $replaceRoot: {
         newRoot: { $mergeObjects: [ { $arrayElemAt: [ "$details", 0 ] }, "$$ROOT" ] }
      }
   },
   {
      $project: { details: 0 }
   }
 ] )
```

The operation returns the following:

```javascript
[
   {
     _id: ObjectId('666b1235eda086b5e22dbcf1'),
     title: 'Tale of Two Cities',
     author: 'Charles Dickens',
     genre: 'Historical Fiction',
     cover_image: '<url>',
     bookId: 1234,
     year: 1859,
     pages: 448,
     price: 15.99,
     description: 'A historical novel set during the French Revolution.'
   }
]
```

In this example, the `$lookup` operation joins the `mainBookInfo` collection with the `additionalBookDetails collection using the id` and `bookId` fields. The :expression:`$mergeObjects` and :pipeline:`$replaceRoot` operations merge the joined documents from the `mainBookInfo` and `additionalBookDetails` collections.

## Learn More

- `schema-design-antipatterns`
- `embedding-vs-references`
