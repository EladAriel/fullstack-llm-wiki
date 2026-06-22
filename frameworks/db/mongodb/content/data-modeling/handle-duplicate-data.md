---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/handle-duplicate-data.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================

# Handle Duplicate Data

.. include:: /includes/data-modeling/data-duplication-overview.rst

## About this Task

One concern with duplicating data is increased storage costs. However, the benefits of optimizing access patterns generally outweigh potential cost increases from storage.

.. include:: /includes/data-modeling/duplicate-data-considerations.rst

## Example: Duplicate Data in an E-Commerce Schema

The following example shows how to duplicate data in an e-commerce application schema to improve data access and performance.

### Steps

The following properties from the `products` collection are duplicated in the `orders` collection:

- `productId`
- `product`
- `price`
- `size`
### Benefits of Duplicating Data

When the application displays order information, it displays the corresponding order's line items. If the order and product information were stored in separate collections, the application would need to perform a :pipeline:`$lookup` to join data from two collections. Lookup operations are often expensive and have poor performance.

The reason to duplicate product information as opposed to only embedding line items in the `orders` collection is that the application only needs a subset of product information when displaying orders. By only embedding the required fields, the application can store additional product details without adding unnecessary bloat to the `orders` collection.

## Example: Duplicate Data for Product Reviews

The following example uses the [subset pattern](https://www.mongodb.com/blog/post/building-with-patterns-the-subset-pattern)_ to optimize access patterns for an online store.

Consider an application where when user views a product, the application displays the product's information and five most recent reviews. The reviews are stored in both a `products` collection and a `reviews` collection.

When a new review is written, the following writes occur:

- The review is inserted into the `reviews` collection.
- The array of recent reviews in the `products` collection is updated
with :update:`$pop` and :update:`$push`.

### Steps

### Benefits of Duplicating Data

The application only needs to make one call to the database to return the all information it needs to display. If data was stored entirely in separate collections, the application would need to join data from the `products` and `reviews` collection, which could cause performance issues.

Reviews are rarely updated, so it is not expensive to store duplicate data and keeping the data consistent between collections is not a challenge.

## Learn More

To learn how to keep duplicate data consistent, see `data-modeling-data-consistency`.
