---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/polymorphic-data/polymorphic-schema-pattern.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
