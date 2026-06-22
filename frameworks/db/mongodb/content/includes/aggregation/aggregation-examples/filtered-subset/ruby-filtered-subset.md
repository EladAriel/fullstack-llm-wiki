---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/filtered-subset/ruby-filtered-subset.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Create the Template App

.. include:: /includes/aggregation/aggregation-examples/template-apps/ruby-template-app.rst

### Create the Collection

This example uses a `persons` collection, which contains documents describing each person's name, date of birth, vocation, and other details. The aggregation selects documents based on whether their field values match specified criteria.

To create the `persons` collection and insert the sample data, add the following code to your application:
