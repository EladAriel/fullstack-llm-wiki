---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-antipatterns/reduce-lookup-operations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# Reduce $lookup Operations

The :pipeline:`$lookup` operator joins information from multiple collections into a single document. While the `$lookup` operation is useful when used infrequently, it can be slow and resource-intensive compared to operations that only query a single collection. If you often use `$lookup` operations, consider restructuring your schema to store related data in a single collection. This can improve query performance and reduce the cost of operations.

## About this Task

Consider the following schema with two separate collections: `products` and `orders`. Each order can contain multiple products, and you want to keep track of product details within each order for quick access. The two separate collections are joined by a `$lookup` operation.

```javascript
 //products collection
 db.products.insertMany( [
    {
       _id: 1,
       name: "Laptop",
       price: 1000,
       manufacturer: "TechCorp",
       category: "Electronics", 
       description: "Fastest computer on the market."
    },
    {
       _id: 2,
       name: "Headphones",
       price: 100,
       manufacturer: "Sound",
       category: "Accessories",
       description: "The latest sound technology."
    },
    {
       _id: 3,
       name: "Tablet",
       price: 200,
       manufacturer: "TechCorp",
       category: "Electronics",
       description: "The most compact tablet."
    }
 ] )
```

```javascript
//orders collection
db.orders.insertMany( [
   {
      _id: 101,
      customer_name: "John Doe",
      timestamp: "2024-05-11T010:00:00Z",
      product_ids: [1, 2],
      total: 1200
   },
   {
      _id: 102,
      customer_name: "Jane Smith",
      timestamp: "2024-05-11T012:00:00Z",
      product_ids: [2],
      total: 100
   }
] )
```

In this schema, you need to use the `$lookup` operation everytime you access order information. Running the `$lookup` operation adds query complexity and degrades performance. To reduce the use of `$lookup` operations, store data that is accessed together in a single collection .

## Example

You can use the subset schema design pattern to embed a subset of product details in the `orders` collection. This lets you query a single collection to return the required results. Product details and documents not relevant to the `orders` collection remain in the `products` collection.

```javascript
//orders collection
db.orders.insertMany( [
   {
      _id: 101,
      customer_name: "John Doe",
      timestamp: "2024-05-11T10:00:00Z",
      products: [
         {
            product_id: 1,
            name: "Laptop",
            price: 1000
         },
         {
            product_id: 2,
            name: "Headphones",
            price: 100
         }
      ],
      total: 1100
   },
   {
      _id: 102,
      customer_name: "Jane Smith",
      timestamp: "2024-05-11T12:00:00Z",
      products: [
         {
            product_id: 2,
            name: "Headphones",
            price: 100
         }
      ],
      total: 100
   }
] )
```

```javascript
 //products collection
 db.products.insertMany( [
    {
       _id: 1,
       name: "Laptop",
       price: 1000,
       manufacturer: "TechCorp",
       category: "Electronics", 
       description: "Fastest computer on the market."
    },
    {
       _id: 2,
       name: "Headphones",
       price: 100,
       manufacturer: "Sound",
       category: "Accessories",
       description: "The latest sound technology."
    },
    {
       _id: 3,
       name: "Tablet",
       price: 200,
       manufacturer: "TechCorp",
       category: "Electronics",
       description: "The most compact tablet."
    }
 ] )
```

This approach lets you keep collections separate while avoiding multiple queries by embedding key fields from the `product` collection into the `orders` collection. This improves read performance and simplifies data retrieval, as you can access all necessary information in a single query. However, it's important to consider potential document size limitations and data duplication.

## Learn More

- `schema-design-antipatterns`
- `schema-design-patterns`
