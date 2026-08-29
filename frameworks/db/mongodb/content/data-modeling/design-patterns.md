---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.771406Z"
---
.. _schema-design-patterns:
.. _data-modeling-patterns:

# Schema Design Patterns

**meta:** :description: Optimize your data model with schema design patterns to enhance query performance and manage schema changes effectively.

.. dismissible-skills-card::
   :skill: Schema Design Patterns & Antipatterns
   :url: https://learn.mongodb.com/skills?openTab=data%20modeling


Use schema design patterns to optimize your data model based on how your
application queries and uses data.

:ref:`schema-design-computed-values`
  Perform calculations in the database so results are ready when the
  client requests data.

:ref:`schema-pattern-group-data`
   Group data into series to improve performance and account for
   outliers.

:ref:`polymorphic-data`
   Handle variable document fields and data types in a single
   collection.

:ref:`schema-pattern-migrations`
   Prepare for schema changes to account for changing technical
   requirements.

:ref:`archive-data-pattern`
   Move old data to a separate location to increase storage and improve
   performance where data is accessed most frequently.

:ref:`data-modeling-single-collection-pattern`
   Use references to group related documents of different types into a
   single collection.

**toctree:** :titlesonly: 
   :hidden: 

   Computed Values </data-modeling/design-patterns/handle-computed-values>
   Group Data </data-modeling/design-patterns/group-data>
   Polymorphic Data </data-modeling/design-patterns/polymorphic-data>
   Versioning </data-modeling/design-patterns/data-versioning>
   Archive Data </data-modeling/design-patterns/archive>
   Single Collection </data-modeling/design-patterns/single-collection>