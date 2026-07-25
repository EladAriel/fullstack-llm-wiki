---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/polymorphic-data.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================

# Polymorphic Data

.. include:: /includes/data-modeling/polymorphic-overview.rst

Generally, documents in a collection are similar in structure but may contain slight variations depending on the application. To group similar, non-identical documents in a single collection you can use the `Polymorphic <polymorphic-schema-pattern>` and the `Inheritance <inheritance-schema-pattern>` schema design patterns.

These schema designs can improve performance by storing data based on query access patterns, rather than storing data strictly based on document shape.

## Use Cases

## Get Started

- `polymorphic-schema-pattern`
- `inheritance-schema-pattern`
## Learn More

- `data-modeling-schema-design`
- `schema-design-patterns`
## Contents

- Polymorphic Pattern </data-modeling/design-patterns/polymorphic-data/polymorphic-schema-pattern>
- Inheritance Pattern </data-modeling/design-patterns/polymorphic-data/inheritance-schema-pattern>
