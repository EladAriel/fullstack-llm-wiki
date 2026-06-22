---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/data-versioning.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Document and Schema Versioning

Your schema may need to change over time to account for changing technical requirements. When your schema changes, you can use schema design patterns to retain your original document structure. By retaining historical versions of documents and schemas, you avoid performance-intensive schema migrations and downtime.

## Use Cases

Use versioning patterns when your data requirements change and you want to keep historical data in its original form. Versioning patterns are most useful when your application meets any of these conditions:

- Application downtime is not an option for migration.
- Updating documents to the new schema may take hours, days, or weeks to
complete.

- Updating documents to the new schema is not a requirement.
Versioning patterns help you decide how data migrations take place and provide more flexibility relative to tabular databases.

Consider these specific application use cases for versioning patterns:

- An insurance company lets customers modify their policy to insure
additional items. When a customer changes their policy, the insurance company keeps a record of the policy changes over time. The company uses the **Document Versioning** pattern to track policy revisions by storing each update in a separate document. Historical data is stored in a separate collection, and does not impact queries on current data.

- A company stores customer contact information. In the original schema,
various contact methods like `homePhone`, `cellPhone`, and `email` are stored in individual fields. Over time, fewer customers have `homePhone` numbers, so the company modifies the schema to move contact information to a generic `contacts` document, which has variable subfields. After the schema change, the company implements the **Schema Versioning** pattern, and adds a `schemaVersion` field to tell the application how it should query each document.

## Tasks

To learn how to keep a history of document and schema changes, see these pages:

- `design-patterns-document-versioning`
- `design-patterns-schema-versioning`
## Learn More

- `data-modeling-schema-design`
- `schema-design-patterns`
- `data-modeling-data-consistency`
## Contents

- Keep Document History </data-modeling/design-patterns/data-versioning/document-versioning>
- Maintain Versions </data-modeling/design-patterns/data-versioning/schema-versioning>
- Slowly Changing Dimensions </data-modeling/design-patterns/data-versioning/slowly-changing-dimensions>
