---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/applications/data-models-relationships.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.725510Z"
---
.. _data-modeling-relationships:

# Document Relationships

**meta:** :description: Explore different ways to model document relationships in MongoDB, including embedded documents and references.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

MongoDB's flexible data model gives you multiple options to map
relationships between different entities in your schema.

Generally, your choice of data model depends on whether you want to
:ref:`embed related data <data-modeling-embedding>` in the same
collection or use :ref:`references <data-modeling-referencing>` to
connect related data that exists in separate collections. Before you
choose a relationship pattern, review :ref:`embedding-vs-references` to
understand the advantages of each approach.

## Get Started

These pages show examples of different data relationships and how to
apply them in a MongoDB schema:

- :ref:`data-modeling-example-one-to-one`

- :ref:`data-modeling-example-one-to-many`

- :ref:`data-modeling-publisher-and-books`

- :ref:`data-modeling-example-many-to-many`

**toctree:** :titlesonly: 
   :hidden: 

   One-to-One Embedded Documents </tutorial/model-embedded-one-to-one-relationships-between-documents>
   One-to-Many Embedded Documents </tutorial/model-embedded-one-to-many-relationships-between-documents>
   One-to-Many References </tutorial/model-referenced-one-to-many-relationships-between-documents>
   Many-to-Many Embedded Documents </tutorial/model-embedded-many-to-many-relationships-between-documents>