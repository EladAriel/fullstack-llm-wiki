---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/group-and-total/scala-group-and-total.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/scala-template-app.rst

### Create the Collection

This example uses an `orders` collection, which contains documents describing individual product orders. Because each order corresponds to only one customer, the aggregation groups order documents by the `customer_id` field, which contains customer email addresses.

To create the `orders` collection and insert the sample data, add the following code to your application:
