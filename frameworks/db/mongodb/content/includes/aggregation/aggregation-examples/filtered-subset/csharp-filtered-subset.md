---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/filtered-subset/csharp-filtered-subset.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/csharp-template-app.rst

### Create the Collection

This example uses a `persons` collection, which contains documents describing each person's name, date of birth, vocation, and other details. The aggregation selects documents based on whether their field values match specified criteria.

First, create C# classes to model the data in the `persons` collection:

To create the `persons` collection and insert the sample data, add the following code to your application:
