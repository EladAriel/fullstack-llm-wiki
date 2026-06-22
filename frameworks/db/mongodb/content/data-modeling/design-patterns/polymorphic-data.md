---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/polymorphic-data.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
