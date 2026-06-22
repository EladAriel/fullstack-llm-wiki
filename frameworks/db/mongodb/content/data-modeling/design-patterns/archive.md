---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/archive.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Archive Pattern

If you need to store historical data dating back a number of years, storing your oldest data in the same database as your more recent data can negatively impact performance, especially if the old data does not need to be accessed frequently. Instead, you can design your schema to archive old data and move that data to a separate storage location.

## About this Task

There are multiple options for how to store your archived data. For example, you can:

- Move data to external file storage such as Amazon S3.
- Move data to a separate, cheaper cluster.
- Move data to a separate collection on the same cluster.
In most cases, moving data to external file storage is the best option in terms of cost and performance. If external file storage is not possible for your use case, consider moving data to a separate cluster or collection.

### Tips for Data Archival

Before you implement a data archival design pattern, review these best practices:

- Your archived data should use an :ref:`embedded data model
<data-modeling-embedding>`, rather than using references to other collections. When you query archived data, all relevant components of the data must be from the same time. Embedding data ensures that queries return the related data together.

- The document's age should be contained in a single field.
- If you have documents that should never expire or move to the archive,
set the document age to `keep forever`, or a similar string to indicate that the document must stay in the active collection.

- MongoDB Atlas offers :atlas:`Online Archive
</online-archive/manage-online-archive/>`, which moves infrequently-accessed data from your Atlas cluster to a MongoDB-managed read-only Federated Database Instance on a cloud object storage.

### Scenario

In this example, an e-commerce store wants to archive data for sales that occurred more than five years ago. The initial dataset contains all sales, and documents for older sales will be moved to a separate collection.

## Steps

## Results

After you run the script, the `sales` collection no longer contains sales that occurred more than five years ago.

```javascript
db.sales.find()
```

Output:

```javascript
[
   {
      _id: ObjectId('679ced18fa29d32ca7d1abab'),
      customer_name: 'Hiroshi Tanaka',
      products: [
         {
            product_id: 'P1001',
            name: 'Wireless Headphones',
            quantity: 1,
            price: 59.99
         },
         {
            product_id: 'P1002',
            name: 'Phone Charger',
            quantity: 2,
            price: 14.99
         }
      ],
      total_amount: 89.97,
      date: ISODate('2025-01-30T10:15:00.000Z')
   },
   {
      _id: ObjectId('679ced18fa29d32ca7d1abae'),
      customer_name: 'Nguyen Minh',
      products: [
         {
            product_id: 'P1008',
            name: 'Bluetooth Speaker',
            quantity: 2,
            price: 39.99
         }
      ],
      total_amount: 79.98,
      date: ISODate('2025-01-26T09:20:00.000Z')
   }
]
```

Old sales now exist in the `archived_sales` collection.

```javascript
db.archived_sales.find()
```

Output:

```javascript
[
   {
      _id: ObjectId('679ced18fa29d32ca7d1abac'),
      customer_name: 'Aisha Khan',
      products: [
         {
            product_id: 'P1003',
            name: 'Laptop',
            quantity: 1,
            price: 899.99
         }
      ],
      total_amount: 899.99,
      date: ISODate('2018-11-20T15:45:00.000Z')
   },
   {
      _id: ObjectId('679ced18fa29d32ca7d1abad'),
      customer_name: 'Fatima Al-Farsi',
      products: [
         {
            product_id: 'P1006',
            name: 'Gaming Mouse',
            quantity: 1,
            price: 49.99
         },
         {
            product_id: 'P1007',
            name: 'Mechanical Keyboard',
            quantity: 1,
            price: 129.99
         }
      ],
      total_amount: 179.98,
      date: ISODate('2017-06-15T12:00:00.000Z')
   }
]
```

## Learn More

- :atlas:`MongoDB Atlas Online Archive
</online-archive/manage-online-archive/>`

- `data-modeling-schema-design`
- `schema-design-antipatterns`
