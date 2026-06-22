---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/group-data/subset-pattern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# Group Data with the Subset Pattern

MongoDB keeps frequently accessed data, referred to as the `working set`, in RAM. When the working set of data and indexes grows beyond the physical RAM allotted, performance is reduced as disk accesses starts to occur and data is no longer retrieved from RAM.

To solve this problem, you can shard your collection. However, sharding can create additional costs and complexities that your application may not be ready for. Rather than sharding your collection, you can reduce the size of your working set by using the subset pattern.

The subset pattern is a data modeling technique used to handle scenarios where you have a large array of items within a document, but need to access frequently a small subset of those items. In this case, the document size can often cause the working set to exceed the computer's RAM capacities. The subset pattern helps optimize performance by reducing the amount of data that needs to be read from the database for common queries.

## About this Task

Consider an e-commerce site that has a list of reviews for a product, stored in a collection called `products`. The e-commerce site inserts documents with the following schema into the `products` collection:

```javascript
db.collection('products').insertOne( [
   {
      _id: ObjectId("507f1f77bcf86cd99338452"),
      name: "Super Widget",
      description: "This is the most useful item in your toolbox."
      price: { value: Decimal128("119.99"), currency: "USD" },
      reviews: [
         {
           review_id: 786,
           review_author: "Kristina",
           review_text: "This is indeed an amazing widgt.",
           published_date: ISODate("2019-02-18")
         },
         {
           review_id: 785,
           review_author: "Trina",
           review_text: "Very nice product, slow shipping.",
           published_date: ISODate("2019-02-17")
         },
         [...],
         {
           review_id: 1,
           review_author: "Hans",
           review_text: "Meh, it's ok.",
           published_date: ISODate("2017-12-06")
         }
      ]  
   }
] )
```

When accessing a product’s data, you likely only need the most recent reviews. The following procedure demonstrates how to apply the subset pattern to the above schema.

## Steps

## Results

By using smaller documents with more frequently accessed data, you reduce the overall size of the working set. This allows for shorter disk access times for the most frequently used information that your application needs.

> **Note:** The subset pattern requires you to manage two collections, rather than one, as well as query
multiple databases when you need to gather comprehensive information on a document, rather than
the subset.
