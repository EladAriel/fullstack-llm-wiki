---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/one-to-one-join/php-one-to-one-join.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/php-template-app.rst

### Create the Collection

This example uses two collections:

- `orders`: documents that describe individual orders for products in a shop
- `products`: documents that describe the products that a shop sells
An order can only contain one product. The aggregation uses a one-to-one join to match an order document to the corresponding product document. The aggregation joins the collections by the `product_id` field that exists in documents in both collections.

To create the `orders` and `products` collections and insert the sample data, add the following code to your application:
