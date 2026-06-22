---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-dot-dollar-import-export-body.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, document field names can be dollar (`$`) prefixed and can contain periods (`.`). However, :binary:`~bin.mongoimport` and :binary:`~bin.mongoexport` may not work as expected in some situations with field names that make use of these characters.

`MongoDB Extended JSON v2 <extended-json-high-level-ref-v2>` cannot differentiate between type wrappers and fields that happen to have the same name as type wrappers. Do not use Extended JSON formats in contexts where the corresponding BSON representations might include dollar (`$`) prefixed keys. The `DBRef <dbref-explanation>` mechanism is an exception to this general rule.

There are also restrictions on using :binary:`~bin.mongoimport` and :binary:`~bin.mongoexport` with periods (`.`) in field names. Since CSV files use the period (`.`) to represent data hierarchies, a period (`.`) in a field name will be misinterpreted as a level of nesting.
