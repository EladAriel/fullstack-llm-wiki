---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/unpack-arrays/nodejs-unpack-arrays.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/nodejs-template-app.rst

### Create the Collection

This example uses an `orders` collection, which contains documents describing product orders. Because each order contains multiple products, the first step of the aggregation unpacks the products array into individual product order documents.

To create the `orders` collection and insert the sample data, add the following code to your application:
