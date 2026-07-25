---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================

# Schema Design Patterns

Use schema design patterns to optimize your data model based on how your application queries and uses data.

`schema-design-computed-values` Perform calculations in the database so results are ready when the client requests data.

`schema-pattern-group-data` Group data into series to improve performance and account for outliers.

`polymorphic-data` Handle variable document fields and data types in a single collection.

`schema-pattern-migrations` Prepare for schema changes to account for changing technical requirements.

`archive-data-pattern` Move old data to a separate location to increase storage and improve performance where data is accessed most frequently.

`data-modeling-single-collection-pattern` Use references to group related documents of different types into a single collection.

## Contents

- Computed Values </data-modeling/design-patterns/handle-computed-values>
- Group Data </data-modeling/design-patterns/group-data>
- Polymorphic Data </data-modeling/design-patterns/polymorphic-data>
- Versioning </data-modeling/design-patterns/data-versioning>
- Archive Data </data-modeling/design-patterns/archive>
- Single Collection </data-modeling/design-patterns/single-collection>
