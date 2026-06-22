---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/unpack-arrays/rust-unpack-arrays.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/rust-template-app.rst

### Create the Collection

This example uses an `orders` collection, which contains documents describing product orders. Because each order contains multiple products, the first step of the aggregation unpacks the products array into individual product order documents.

First, create Rust structs to model the data in the `orders` collection:

To create the `orders` collection and insert the sample data, add the following code to your application:
