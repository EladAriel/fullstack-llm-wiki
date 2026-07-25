---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/multi-field-join/scala-multi-field-join.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/scala-template-app.rst

### Create the Collection

This example uses two collections:

- `products`, which contains documents describing the products that a shop sells
- `orders`, which contains documents describing individual orders for products in a shop
An order can only contain one product. The aggregation uses a multi-field join to match a product document to documents representing orders of that product. The aggregation joins collections by the `name` and `variation` fields in documents in the `products` collection, corresponding to the `product_name` and `product_variation` fields in documents in the `orders` collection.

To create the `products` and `orders` collections and insert the sample data, add the following code to your application:
