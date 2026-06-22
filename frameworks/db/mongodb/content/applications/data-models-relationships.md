---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/applications/data-models-relationships.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# Document Relationships

MongoDB's flexible data model gives you multiple options to map relationships between different entities in your schema.

Generally, your choice of data model depends on whether you want to `embed related data <data-modeling-embedding>` in the same collection or use `references <data-modeling-referencing>` to connect related data that exists in separate collections. Before you choose a relationship pattern, review `embedding-vs-references` to understand the advantages of each approach.

## Get Started

These pages show examples of different data relationships and how to apply them in a MongoDB schema:

- `data-modeling-example-one-to-one`
- `data-modeling-example-one-to-many`
- `data-modeling-publisher-and-books`
- `data-modeling-example-many-to-many`
## Contents

- One-to-One Embedded Documents </tutorial/model-embedded-one-to-one-relationships-between-documents>
- One-to-Many Embedded Documents </tutorial/model-embedded-one-to-many-relationships-between-documents>
- One-to-Many References </tutorial/model-referenced-one-to-many-relationships-between-documents>
- Many-to-Many Embedded Documents </tutorial/model-embedded-many-to-many-relationships-between-documents>
