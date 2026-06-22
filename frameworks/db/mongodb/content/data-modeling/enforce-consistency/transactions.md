---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/enforce-consistency/transactions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# Enforce Data Consistency with Transactions

You can use `transactions <transactions>` to enforce consistency between collections that contain duplicated data. Transactions update multiple collections in a single atomic operation.

Use transactions to enforce consistency if your application must always return up-to-date data and can tolerate potential negative performance impact during periods of heavy reads.

Transactions might not be as performant as other methods of enforcing data consistency. Read performance might be negatively impacted while a transaction is open. However, transactions ensure that the data read by the client is always current.

## About this Task

To use transactions, you must connect to a replica set or sharded cluster. You cannot use transactions on standalone deployments.

## Before you Begin

.. include:: /includes/data-modeling/data-consistency/before-you-begin.rst

## Steps

The following example enforces data consistency in an e-commerce application. The example schema duplicates product information in the `products` and `sellers` collections. This schema design optimizes queries for both products and sellers.

When a product is updated, such as when its price changes, it is critical that the price is consistent in the `products` and `sellers` collections. Therefore, transactions are a reasonable method to enforce data consistency in this application.

## Results

To confirm that the price was updated and that the data is consistent, query the `products` and `sellers` collections.

### Query the Products Collection

```javascript
db.products.find( { sellerId: 456, name: "vest" } )
```

Output:

```javascript
[
   {
     _id: ObjectId("64d506c3ddebf45734d06c58"),
     sellerId: 456,
     name: 'vest',
     price: 25,
     rating: 4.7
   } 
]
```

### Query the Sellers Collection

```javascript
db.sellers.find( { id: 456, "products.name": "vest" } )
```

Output:

```javascript
[
   {
     _id: ObjectId("64d516d9ddebf45734d06c5a"),
     id: 456,
     name: 'Cool Clothes Co',
     location: {
       address: '21643 Andreane Shores',
       state: 'Ohio',
       country: 'United States'
     },
     phone: '567-555-0105',
     products: [
       { name: 'sweater', price: 30 },
       { name: 't-shirt', price: 10 },
       { name: 'vest', price: 25 }
     ]
   }
]
```

## Learn More

To see other ways to enforce data consistency, see:

- :atlas:`Atlas Database Triggers
</atlas-ui/triggers/database-triggers>`

- `enforce-consistency-embedding`
