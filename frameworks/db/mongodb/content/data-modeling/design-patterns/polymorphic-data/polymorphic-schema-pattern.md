---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/polymorphic-data/polymorphic-schema-pattern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# Store Polymorphic Data

Store polymorphic data when you need to access documents that have different fields or data types together in the same query.

.. include:: /includes/data-modeling/polymorphic-overview.rst

## About this Task

In this example, your application stores professional athletes who play different sports. Your queries access all athletes, but the attributes stored for each athlete vary depending on their sport.

The polymorphic pattern stores different document shapes in the same collection, which improves performance for queries that need to access all athletes regardless of sport.

## Steps

## Learn More

- `inheritance-schema-pattern`
- `schema-validation-overview`
- `create-indexes-to-support-queries`
