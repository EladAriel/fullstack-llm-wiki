---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/multi-field-join/php-multi-field-join.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/golang-template-app.rst

### Create the Collection

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop
An order can only contain one product. The aggregation uses a multi-field join to match a product document to documents representing orders of that product. The aggregation joins collections by the `name` and `variation` fields in documents in the `products` collection, corresponding to the `product_name` and `product_variation` fields in documents in the `orders` collection.

To create the `products` and `orders` collections and insert the sample data, add the following code to your application:
